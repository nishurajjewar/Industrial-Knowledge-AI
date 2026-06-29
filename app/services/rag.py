from app.services.retriever import search
from app.services.gemini import ask_gemini


def ask_pdf(question):

    results = search(question)

    context = ""

    if "documents" in results and len(results["documents"]) > 0:

        context = "\n\n".join(results["documents"][0])

    prompt = f"""
You are an Industrial Knowledge Assistant.

Answer ONLY using the context below.

If the answer is not present in the context,
reply with:

"I could not find the answer in the uploaded documents."

Context:

{context}

Question:

{question}

Answer:
"""

    answer = ask_gemini(prompt)

    return answer