from app.database.connection import engine
from app.database.base import Base

from app.models.document_content import DocumentContent

from app.models.chat_history import ChatHistory

from app.models.document import Document

Base.metadata.create_all(bind=engine)

print("Database tables created successfully")
