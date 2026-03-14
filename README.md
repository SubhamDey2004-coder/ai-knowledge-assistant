# AI Knowledge Assistant for Company Documents

This project is a Retrieval-Augmented Generation (RAG) system that allows users to upload PDF documents and ask questions about them using an AI assistant.

The system processes uploaded documents, converts them into embeddings, stores them in a FAISS vector database, and retrieves relevant information to generate answers using a local LLM.

---

## Features

* Upload company documents (PDF)
* Automatic document processing and indexing
* Semantic search using FAISS
* Local LLM inference using Ollama
* Multi-document question answering
* Source citation for answers
* Simple chat interface

---

## Tech Stack

Backend

* Python
* FastAPI
* FAISS
* Sentence Transformers
* Ollama (Local LLM)

Frontend

* HTML
* TailwindCSS
* JavaScript

Database

* MySQL (for document metadata)

---

## Project Architecture

User Question
↓
Embedding Generation
↓
Vector Search (FAISS)
↓
Relevant Document Chunks Retrieved
↓
Local LLM Generates Answer
↓
Answer + Source Returned to UI

---

## Installation

Clone the repository

```
git clone https://github.com/SubhamDey2004-coder/ai-knowledge-assistant.git
cd ai-knowledge-assistant
```

Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

Install dependencies

```
pip install -r backend/requirements.txt
```

---

## Run Backend

```
cd backend
uvicorn app.main:app --reload
```

Backend will start at

```
http://127.0.0.1:8000
```

---

## Run Frontend

Open the file

```
frontend/index.html
```

in your browser.

---

## Usage

1. Upload a PDF document.
2. Ask questions about the document.
3. The AI retrieves relevant context and generates an answer.
4. The source document is displayed with the response.

---

## Example Questions

```
What is the internship domain?
What are the workplace safety rules?
What protective equipment must employees wear?
```

---

## Future Improvements

* Authentication system
* Streaming responses
* Conversation memory
* Document filtering
* Cloud deployment

---
