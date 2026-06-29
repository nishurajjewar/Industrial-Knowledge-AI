from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.rag import ask_pdf
from app.memory.chat_memory import clear_history

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
def chat(request: ChatRequest):

    try:

        result = ask_pdf(request.question)

        return {
            "status": "success",
            "question": request.question,
            "answer": result["answer"],
            "confidence": result["confidence"],
            "sources": result["sources"]
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.post("/clear-chat")
def clear_chat():

    clear_history()

    return {
        "status": "success",
        "message": "Conversation Cleared Successfully"
    }