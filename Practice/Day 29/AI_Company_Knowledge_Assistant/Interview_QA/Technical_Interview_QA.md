# Technical Interview Q&A — AI Company Knowledge Assistant

## 1. What is RAG?
RAG stands for Retrieval-Augmented Generation. It retrieves relevant information from a knowledge base and supplies it to an LLM before generating an answer.

## 2. Why use RAG?
It helps ground responses in company-specific information and reduces unsupported answers.

## 3. What is an embedding?
An embedding is a numerical vector representation of text used for semantic similarity search.

## 4. Why ChromaDB?
ChromaDB is used as the vector store for document embeddings and similarity retrieval.

## 5. Why chunk documents?
Large documents are divided into smaller pieces so relevant sections can be retrieved efficiently.

## 6. What model generates embeddings?
The project uses `nomic-embed-text` through Ollama.

## 7. What LLM generates answers?
The project uses Llama 3.2 through Ollama.

## 8. What happens for unsupported questions?
The system is instructed not to invent information and should respond that the requested information is unavailable from the supplied documentation.

## 9. Why create a fresh ChromaDB?
Repeated runs against persistent data can create duplicate chunks. A fresh database gives clean and repeatable testing.

## 10. What are current limitations?
The current version uses one text document and a terminal interface. Future improvements could include a web UI, multiple document formats, better ranking, authentication, conversation history, and deployment.
