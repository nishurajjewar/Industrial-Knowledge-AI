from app.services.retriever import search
from app.services.gemini import ask_gemini
from app.prompts.rag_prompt import RAG_PROMPT

from app.memory.chat_memory import (
    add_message,
    get_history
)


def ask_pdf(question):

    # Save user question
    add_message("User", question)

    # Search ChromaDB
    results = search(question)

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
    confidence = round((1 - results["distances"][0][0]) * 100, 2)

    return {
        "answer": answer,
        "confidence": confidence,
        "sources": results["documents"][0]
    }