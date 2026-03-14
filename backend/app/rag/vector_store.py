import faiss
import numpy as np
import os
import pickle

dimension = 384

INDEX_PATH = "vector_index.faiss"
DOC_PATH = "documents.pkl"

# FAISS index
index = faiss.IndexFlatL2(dimension)

# Each item will store:
# { "text": chunk_text, "source": filename }
documents = []


def add_embedding(embedding, text, source):

    vector = np.array([embedding]).astype("float32")

    index.add(vector)

    documents.append({
        "text": text,
        "source": source
    })

    save_index()


def search_similar(query_embedding, k=3):

    if len(documents) == 0:
        return []

    vector = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(vector, k)

    results = []

    for i in indices[0]:
        if i != -1 and i < len(documents):
            results.append(documents[i])

    return results


def save_index():

    faiss.write_index(index, INDEX_PATH)

    with open(DOC_PATH, "wb") as f:
        pickle.dump(documents, f)


def load_index():

    global index, documents

    if os.path.exists(INDEX_PATH) and os.path.exists(DOC_PATH):

        index = faiss.read_index(INDEX_PATH)

        with open(DOC_PATH, "rb") as f:
            documents = pickle.load(f)