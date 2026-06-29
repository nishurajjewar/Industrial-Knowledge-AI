from fastapi import APIRouter
from pydantic import BaseModel

from app.services.rag import ask_pdf

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
def chat(request: ChatRequest):

    answer = ask_pdf(request.question)

    return {
        "question": request.question,
        "answer": answer
    }