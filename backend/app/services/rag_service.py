from app.rag.embedding_model import generate_embedding
from app.rag.vector_store import search_similar
from app.rag.local_llm import generate_answer_stream

def ask_question(question: str):
    
    query_embedding = generate_embedding(question)
    
    chunks = search_similar(query_embedding)
    print("Retrieved chunks:", chunks)
    context = "\n".join([c["text"] for c in chunks])
    
    print("Retrieved Context:", context)
    
    answer = generate_answer_stream(question, context)
    
    sources = list(set([c["source"] for c in chunks]))
    
    return {
        "answer": answer,
        "sources": sources
    }
    
    
def ask_question_stream(question: str):

    question_lower = question.lower()

    if question_lower in ["thanks", "thank you", "ok", "great", "good", "nice"]:
        return iter(["You're welcome! Let me know if you have another question about the document."]), []

    query_embedding = generate_embedding(question)

    chunks = search_similar(query_embedding)

    context = "\n".join([c["text"] for c in chunks])

    sources = []
    for c in chunks:
        if c["source"] not in sources:
            sources.append(c["source"])

    print("Retrieved chunks:", chunks)
    print("Retrieved Context:", context)

    stream = generate_answer_stream(question, context)

    return stream, sources