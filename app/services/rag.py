from app.services.retriever import search
from app.services.gemini import ask_gemini


def ask_pdf(question):

    results = search(question)

    context = "\n".join(results["documents"][0])

    prompt = f"""
You are an AI assistant.

Answer the question only from the given context.

Context:
{context}

Question:
{question}
"""

    answer = ask_gemini(prompt)

    return {
        "answer": answer,
        "source": results["documents"][0],
        "distance": results["distances"][0]
    }