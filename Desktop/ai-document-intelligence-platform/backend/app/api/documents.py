from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
import os

from app.database.session import get_db
from app.models.document import Document

from app.services.pdf_service import (
    extract_text_from_pdf,
    chunk_text
)

from app.services.vector_db import (
    store_chunks
)

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    try:
        print("===== UPLOAD STARTED =====")

        if not file.filename.lower().endswith(".pdf"):
            raise HTTPException(
                status_code=400,
                detail="Only PDF files are supported"
            )

        file_path = os.path.join(
            UPLOAD_DIR,
            file.filename
        )

        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        print("STEP 1: File Saved")
        print("File Path:", file_path)

        text = extract_text_from_pdf(file_path)

        print("STEP 2: Text Extracted")
        print("Text Length:", len(text))

        chunks = chunk_text(text)

        print("STEP 3: Chunks Created")
        print("Chunk Count:", len(chunks))

        store_chunks(chunks)

        print("STEP 4: Stored In Chroma")

        document = Document(
            filename=file.filename,
            file_path=file_path,
            status="processed"
        )

        db.add(document)
        db.commit()
        db.refresh(document)

        print("STEP 5: Database Updated")
        print("===== UPLOAD SUCCESS =====")

        return {
            "id": document.id,
            "filename": document.filename,
            "chunks": len(chunks),
            "status": "processed"
        }

    except Exception as e:
        print("===== ERROR =====")
        print(str(e))

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )