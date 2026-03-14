from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database.database import Base

class Document(Base):
    __tablename__ = "documents"
    
    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String(255))
    file_path = Column(String(500))
    upload_date = Column(DateTime, default=lambda: datetime.now(datetime.timezone.utc))
