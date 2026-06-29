from fastapi import APIRouter
from pydantic import BaseModel
from app.services.rag import ask_pdf

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
def chat(request: ChatRequest):

    result = ask_pdf(request.question)

    return {
        "status": "success",
        "question": request.question,
        "answer": result["answer"],
        "source": result["source"],
        "distance": result["distance"]
    }