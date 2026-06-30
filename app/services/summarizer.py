from app.services.retriever import search
from app.services.gemini import ask_gemini


def summarize_documents():

    # Search relevant documents
    results = search("Summarize all uploaded documents")

    # Create context
    context = "\n".join(results["documents"][0])

    # Prompt for Gemini
    prompt = f"""
You are an Industrial Knowledge Assistant.

Using ONLY the provided context, generate a professional summary.

Context:

{context}

Output Format:

Summary:
(5-10 lines)

Key Topics:
- ...
- ...
- ...

Important Points:
1.
2.
3.
4.

Do not invent information that is not present in the context.
"""

    # Get summary from Gemini
    answer = ask_gemini(prompt)

    return answer