# AI Knowledge Assistant for Company Documents

A document-grounded question-answering application that lets users upload PDF documents, retrieve relevant information semantically, and generate answers using a local language model.

## Problem

Finding specific information inside multiple company documents can be slow and error-prone. This project implements a RAG-style workflow that combines semantic retrieval with local LLM generation.

## Architecture

```text
PDF Documents
      ↓
Document Processing
      ↓
Embedding Generation
      ↓
FAISS Vector Database
      ↓
Semantic Retrieval
      ↓
Relevant Context
      ↓
Local LLM (Ollama)
      ↓
Answer + Source
```

## Features

- PDF document upload
- Automatic document processing and indexing
- Semantic search with FAISS
- Sentence Transformer embeddings
- Local LLM inference with Ollama
- Multi-document question answering
- Source citation in responses
- Simple browser-based chat interface

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI |
| Language | Python |
| Embeddings | Sentence Transformers |
| Vector database | FAISS |
| LLM runtime | Ollama |
| Metadata database | MySQL |
| Frontend | HTML, TailwindCSS, JavaScript |

## Project Structure

```text
ai-knowledge-assistant/
├── backend/
│   ├── app/
│   └── requirements.txt
├── frontend/
│   └── index.html
└── README.md
```

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/SubhamDey2004-coder/ai-knowledge-assistant.git
cd ai-knowledge-assistant
```

### 2. Create an environment

```bash
python -m venv venv
```

Windows:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r backend/requirements.txt
```

### 4. Start the backend

```bash
cd backend
uvicorn app.main:app --reload
```

### 5. Open the frontend

Open `frontend/index.html` in a browser.

## Example Use Cases

The assistant can be used for questions such as:

- What are the workplace safety rules?
- What protective equipment is required?
- What does the uploaded policy say about a particular process?

## Engineering Focus

This project demonstrates a complete retrieval-to-generation workflow:

- Document ingestion
- Embedding generation
- Vector similarity search
- Context retrieval
- Local LLM generation
- Source-aware responses
- FastAPI backend integration

## Future Improvements

- Authentication
- Conversation memory
- Streaming responses
- Metadata filtering
- Evaluation of retrieval quality and answer faithfulness
- Cloud deployment

## Author

**Subham Dey**
