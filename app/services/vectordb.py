import chromadb
import uuid

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="industrial_docs"
)

def store_embeddings(chunks, embeddings):

    ids = [str(uuid.uuid4()) for _ in chunks]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist()
    )