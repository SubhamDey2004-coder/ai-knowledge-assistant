from fastapi import APIRouter, UploadFile, File, Depends
import shutil
import os
from app.services.document_service import get_all_documents
from app.services.document_service import delete_document
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.services.document_service import save_document_metadata
from app.services.document_service import get_documents_from_db
from app.services.rag_service import ask_question
from app.services.rag_service import ask_question_stream
from pydantic import BaseModel
from app.rag.retriever import process_document

router = APIRouter()
UPLOAD_DIR = "uploads"

class QuestionRequest(BaseModel):
    question: str

@router.post("/upload_document")
async def upload_document(file: UploadFile = File(...), db: Session = Depends(get_db)):

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Save metadata in MySQL
    save_document_metadata(db, file.filename, file_path)

    # Process document for RAG
    process_document(file_path)

    return {
        "message": "Document uploaded and indexed successfully",
        "filename": file.filename
    }
    
@router.get("/documents")
def list_documents(db: Session = Depends(get_db)):
    documents = get_documents_from_db(db)
    
    return {
        "documents": [
            {
                "id": doc.id,
                "file_name": doc.file_name,
                "upload_date": doc.upload_date
            }
            for doc in documents
        ]
    }
    
@router.delete("/documents/{filename}")
def remove_document(filename: str):
    
    deleted = delete_document(filename)
    
    if not deleted:
        return {"error": "Document not found"}
    
    return {"message": "Document deleted successfully"}

@router.post("/ask")
def ask_ai(request: QuestionRequest):

    stream, sources = ask_question_stream(request.question)

    answer = "".join(list(stream))

    return {
        "answer": answer.strip(),
        "sources": sources
    }