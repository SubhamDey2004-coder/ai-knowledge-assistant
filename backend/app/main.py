from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import documents_routes
from app.database.database import engine
from app.models import document_model
from app.rag.vector_store import load_index

document_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_index()

app.include_router(documents_routes.router)

@app.get("/")
def root():
    return {"message": "AI Knowledge Assistant API running"}