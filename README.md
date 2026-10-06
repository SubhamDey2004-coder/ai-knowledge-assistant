# AI Knowledge Assistant for Company Documents

A document-grounded question-answering application that lets users upload PDF documents, retrieve relevant information semantically, and generate answers with a local language model.

## What it does

1. Uploads PDF documents through a FastAPI endpoint.
2. Extracts and chunks document text.
3. Generates embeddings with Sentence Transformers.
4. Stores embeddings and source metadata in a local FAISS index.
5. Retrieves the most relevant chunks for a question.
6. Generates an answer with a local Ollama model.
7. Returns the answer together with document sources.

## Architecture

~~~text
PDF Upload
    ↓
PDF Text Extraction
    ↓
Recursive Chunking
    ↓
Sentence Transformer Embeddings
    ↓
FAISS Vector Store
    ↓
Similarity Retrieval
    ↓
Relevant Context
    ↓
Local Ollama LLM
    ↓
Answer + Sources
~~~

## Features

- PDF document upload and indexing
- Semantic retrieval with FAISS
- Sentence Transformer embeddings
- Local LLM inference with Ollama
- Multi-document question answering
- Source-aware responses
- MySQL document metadata storage
- Simple browser-based frontend

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI |
| Language | Python |
| Embeddings | Sentence Transformers |
| Vector store | FAISS |
| LLM runtime | Ollama |
| Metadata database | MySQL + SQLAlchemy |
| PDF processing | pypdf |
| Frontend | HTML, JavaScript, TailwindCSS |

## Project Structure

~~~text
ai-knowledge-assistant/
├── backend/
│   ├── app/
│   │   ├── database/
│   │   ├── models/
│   │   ├── rag/
│   │   ├── routes/
│   │   └── services/
│   └── requirements.txt
├── frontend/
│   └── index.html
├── assets/
│   └── image.png
├── .gitignore
└── README.md
~~~

## Run Locally

### 1. Create an environment

~~~bash
python -m venv .venv
~~~

Windows:

~~~powershell
.\.venv\Scripts\Activate.ps1
~~~

### 2. Install dependencies

~~~bash
pip install -r backend/requirements.txt
~~~

### 3. Configure MySQL

Create a MySQL database named:

~~~text
ai_knowledge_assistant
~~~

Set the connection string through the `DATABASE_URL` environment variable:

~~~powershell
$env:DATABASE_URL="mysql+pymysql://root:YOUR_PASSWORD@localhost/ai_knowledge_assistant"
~~~

Do not commit database credentials.

### 4. Start Ollama

Make sure Ollama is running locally and the `tinyllama` model is available.

### 5. Start the backend

From the repository root:

~~~bash
cd backend
uvicorn app.main:app --reload
~~~

The API will be available at `http://127.0.0.1:8000`.

### 6. Open the frontend

Open `frontend/index.html` in a browser.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/upload_document` | Upload and index a PDF |
| GET | `/documents` | List uploaded document metadata |
| DELETE | `/documents/{filename}` | Delete an uploaded file |
| POST | `/ask` | Ask a question over indexed documents |

FastAPI also provides interactive documentation at `/docs`.

## Example Questions

- What are the workplace safety rules?
- What protective equipment is required?
- What does the uploaded policy say about a particular process?

## Engineering Focus

This project demonstrates:

- Document ingestion and preprocessing
- Text chunking
- Dense vector embeddings
- FAISS similarity search
- Retrieval-augmented generation
- Local LLM inference
- Source tracking
- FastAPI backend integration
- MySQL-backed document metadata

## Limitations

- The application currently expects Ollama and MySQL to be available locally.
- The frontend uses a fixed local backend URL for development.
- Retrieval quality depends on document quality, chunking, and embedding similarity.
- The project is a prototype and does not yet include authentication or production deployment.

## Future Improvements

- Authentication and authorization
- Conversation memory
- Streaming responses
- Metadata-aware retrieval and filtering
- Retrieval and answer-quality evaluation
- Production deployment

## Author

**Subham Dey**
