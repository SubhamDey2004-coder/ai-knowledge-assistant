import os
from sqlalchemy.orm import Session
from app.models.document_model import Document
from datetime import datetime, timezone


UPLOAD_DIR = "uploads"

def get_all_documents():
    
    if not os.path.exists(UPLOAD_DIR):
        return []
    
    files = os.listdir(UPLOAD_DIR)
    
    return files

def delete_document(filename):
    
    file_path = os.path.join(UPLOAD_DIR, filename)
    
    if not os.path.exists(file_path):
        return False
    os.remove(file_path)
    
    return True

def save_document_metadata(db: Session, file_name: str, file_path: str):
    document = Document(
        file_name=file_name,
        file_path=file_path,
        upload_date=datetime.now(timezone.utc)
    )
    
    db.add(document)
    db.commit()
    db.refresh(document)
    
    return document
    
def get_documents_from_db(db: Session):
    documents = db.query(Document).all()
    
    return documents