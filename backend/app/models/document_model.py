from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Integer, String

from app.database.database import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String(255), nullable=False)
    file_path = Column(String(500), nullable=False)
    upload_date = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
