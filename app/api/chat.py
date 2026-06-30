from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.rag import ask_pdf
from app.services.recommendation import get_recommendation
from app.services.summarizer import summarize_documents
from app.services.analytics import get_analytics
from app.memory.chat_memory import clear_history

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


class RecommendationRequest(BaseModel):
    symptom: str


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


@router.post("/recommend")
def recommend(request: RecommendationRequest):

    try:

        answer = get_recommendation(request.symptom)

        return {
            "status": "success",
            "symptom": request.symptom,
            "recommendation": answer
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.post("/summarize")
def summarize():

    try:

        summary = summarize_documents()

        return {
            "status": "success",
            "summary": summary
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


@router.get("/analytics")
def analytics():

    try:

        data = get_analytics()

        return {
            "status": "success",
            "analytics": data
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )