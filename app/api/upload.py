from fastapi import APIRouter, UploadFile, File
import shutil
import os

from app.services.parser import extract_text
from app.services.cleaner import clean_text
from app.services.chunker import chunk_text
from app.services.embedding import generate_embeddings
from app.services.vectordb import store_embeddings

router = APIRouter()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    # Save PDF
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    if os.path.exists(file_path):
        return {
        "status": "failed",
        "message": "PDF already exists.",
        "filename": file.filename
    }

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract Text
    text = extract_text(file_path)

    # Clean Text
    cleaned = clean_text(text)

    # Chunk Text
    chunks = chunk_text(cleaned)

    # Generate Embeddings
    embeddings = generate_embeddings(chunks)

    # Store in ChromaDB
    store_embeddings(
    chunks,
    embeddings,
    file.filename
)

    return {
        "status": "success",
        "message": "PDF Uploaded and Indexed Successfully",
        "filename": file.filename,
        "chunks": len(chunks)
    }