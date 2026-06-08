from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.chat import ChatRequest
from app.services.retrieval_service import retrieve_context
from app.services.llm_service import ask_llm

from app.database.session import get_db
from app.models.chat_history import ChatHistory

router = APIRouter()


@router.post("/")
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
):
    context = retrieve_context(
        request.question
    )

    answer = ask_llm(
        context,
        request.question
    )

    chat_record = ChatHistory(
        question=request.question,
        answer=answer
    )

    db.add(chat_record)
    db.commit()

    return {
        "answer": answer
    }


@router.get("/history")
def get_chat_history(
    db: Session = Depends(get_db)
):
    chats = (
        db.query(ChatHistory)
        .order_by(ChatHistory.created_at.desc())
        .all()
    )

    return [
        {
            "id": chat.id,
            "question": chat.question,
            "answer": chat.answer,
            "created_at": chat.created_at
        }
        for chat in chats
    ]