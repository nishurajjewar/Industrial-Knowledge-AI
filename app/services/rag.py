from app.services.query_logger import log_query
from app.services.retriever import search
from app.services.gemini import ask_gemini
from app.prompts.rag_prompt import RAG_PROMPT
from app.services.gap_detector import check_gap

from app.memory.chat_memory import (
    add_message,
    get_history
)


def ask_pdf(question):

    # Save user question
    add_message("User", question)

    # Save query in logs
    log_query(question)

    # Search ChromaDB
    results = search(question)

    # Check if any relevant document exists
    if check_gap(results):
        return {
            "answer": "❌ This topic is not available in the uploaded documents.\n\nPlease upload a document related to this topic.",
            "confidence": 0,
            "sources": []
        }

    # Create context
    context = "\n".join(results["documents"][0])

    # Previous Conversation
    history = ""

    for chat in get_history():
        history += f"{chat['role']}: {chat['message']}\n"

    # Create Prompt
    prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )

    prompt += f"""

Conversation History:

{history}
"""

    # Ask Gemini
    answer = ask_gemini(prompt)

    # Save AI response
    add_message("Assistant", answer)

    # Confidence Score
    try:
        confidence = round((1 - results["distances"][0][0]) * 100, 2)
    except Exception:
        confidence = 0

    return {
        "answer": answer,
        "confidence": confidence,
        "sources": results["documents"][0]
    }