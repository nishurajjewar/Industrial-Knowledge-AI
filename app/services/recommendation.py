from app.services.retriever import search
from app.services.gemini import ask_gemini


def get_recommendation(symptom):

    print("STEP 1 : Recommendation Started")

    results = search(symptom)

    print("STEP 2 : Search Completed")

    context = "\n".join(results["documents"][0])

    print("STEP 3 : Context Created")

    prompt = f"""
You are an Industrial Maintenance Expert.

Symptom:
{symptom}

Context:
{context}

Give:

1. Probable Causes
2. Inspection Steps
3. Priority
"""

    print("STEP 4 : Prompt Ready")

    answer = ask_gemini(prompt)

    print("STEP 5 : Gemini Response Received")

    return answer