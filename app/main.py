from app.api.chat import router as chat_router
from app.services.gemini import ask_gemini
from app.services.retriever import search
from app.services.vectordb import store_embeddings
from app.services.embedding import generate_embeddings
from app.services.chunker import chunk_text
from app.services.cleaner import clean_text
from fastapi import FastAPI
from app.services.parser import extract_text

app = FastAPI(
    title="Industrial Knowledge AI",
    version="1.0.0"
)

app.include_router(chat_router)

@app.get("/")
def home():
    return {
        "message": "AI Service is Running 🚀"
    }

@app.get("/test")
def test():

    text = extract_text("uploads/manual.pdf")

    cleaned = clean_text(text)

    chunks = chunk_text(cleaned)

    embeddings = generate_embeddings(chunks)

    store_embeddings(chunks, embeddings)

    return {

        "Status":"Stored Successfully",

        "Chunks":len(chunks)

    }

@app.get("/search")
def semantic_search(query: str):

    documents = search(query)

    return {
        "query": query,
        "results": documents
    }
@app.get("/gemini-test")
def gemini_test():

    answer = ask_gemini("Say Hello from Gemini AI")

    return {
        "response": answer
    }