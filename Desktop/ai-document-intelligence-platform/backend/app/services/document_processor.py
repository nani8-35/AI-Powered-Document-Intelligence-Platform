from app.services.chunk_service import chunk_text
from app.services.embedding_service import generate_embedding
from app.services.vector_db import collection
import uuid

def process_document(text):
    chunks = chunk_text(text)

    for chunk in chunks:
        collection.add(
            ids=[str(uuid.uuid4())],
            documents=[chunk],
            embeddings=[generate_embedding(chunk)]
        )

    print(f"{len(chunks)} chunks stored")