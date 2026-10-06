import os
import pickle

import faiss
import numpy as np


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
INDEX_PATH = os.path.join(BASE_DIR, "vector_index.faiss")
DOC_PATH = os.path.join(BASE_DIR, "documents.pkl")

EMBEDDING_DIMENSION = 384

index = faiss.IndexFlatL2(EMBEDDING_DIMENSION)
documents = []


def add_embedding(embedding, text, source):
    vector = np.asarray([embedding], dtype="float32")
    index.add(vector)
    documents.append({"text": text, "source": source})
    save_index()


def search_similar(query_embedding, k=3):
    if not documents:
        return []

    vector = np.asarray([query_embedding], dtype="float32")
    k = min(k, len(documents))
    _, indices = index.search(vector, k)

    return [
        documents[i]
        for i in indices[0]
        if i != -1 and i < len(documents)
    ]


def save_index():
    faiss.write_index(index, INDEX_PATH)

    with open(DOC_PATH, "wb") as file:
        pickle.dump(documents, file)


def load_index():
    global index, documents

    if not (os.path.exists(INDEX_PATH) and os.path.exists(DOC_PATH)):
        return

    index = faiss.read_index(INDEX_PATH)

    with open(DOC_PATH, "rb") as file:
        documents = pickle.load(file)
