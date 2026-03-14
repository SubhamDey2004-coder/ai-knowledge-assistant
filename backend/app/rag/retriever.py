import os

from app.rag.pdf_processor import extract_text_from_pdf, split_text_into_chunks
from app.rag.embedding_model import generate_embedding
from app.rag.vector_store import add_embedding


def process_document(file_path):

    text = extract_text_from_pdf(file_path)

    chunks = split_text_into_chunks(text)

    filename = os.path.basename(file_path)

    for chunk in chunks:
        embedding = generate_embedding(chunk)
        add_embedding(embedding, chunk, filename)