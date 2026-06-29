import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="industrial_docs"
)

model = None

def get_model():
    global model

    if model is None:
        print("Loading AI Model...")
        model = SentenceTransformer("all-MiniLM-L6-v2")

    return model


def search(query):

    model = get_model()

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    return results["documents"][0]