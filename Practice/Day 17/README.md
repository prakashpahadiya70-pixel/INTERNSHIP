# Day 17 - Complete RAG API

## 📌 Project Title

**Complete RAG API using FastAPI, Hugging Face, ChromaDB and Gemini**

---

## 🎯 Objective

The objective of this project is to build a Retrieval-Augmented Generation (RAG) API that allows users to:

1. Upload PDF documents.
2. Process and split the document into smaller chunks.
3. Generate embeddings using a Hugging Face embedding model.
4. Store document chunks in ChromaDB.
5. Ask questions related to the uploaded document.
6. Retrieve relevant document chunks.
7. Generate answers using Gemini.
8. Return the answer along with the document source.

The API is developed using **FastAPI** and can be tested through the automatically generated Swagger UI.

---

# 📚 Learning Objectives

During Day 17, the following concepts were implemented:

- FastAPI
- File Upload
- Document Processing
- PDF Processing
- Chunking
- Metadata
- Vector Embeddings
- ChromaDB
- Retrieval-Augmented Generation (RAG)
- API Endpoints
- API Testing
- Error Handling
- Robustness Testing

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | REST API development |
| Uvicorn | FastAPI server |
| PyPDF | PDF document loading |
| LangChain | RAG pipeline |
| Hugging Face | Text embeddings |
| Sentence Transformers | Embedding model |
| ChromaDB | Vector database |
| Google Gemini | Answer generation |
| Pydantic | Request validation |
| python-dotenv | Environment variable management |
| Swagger UI | API testing |

---

# 🤖 Models Used

## Embedding Model

```text
sentence-transformers/all-MiniLM-L6-v2