# AI Company Knowledge Assistant

A Retrieval-Augmented Generation (RAG) based company knowledge assistant built for Day 29.

## Objective

Provide grounded answers to employee questions using company documentation instead of unsupported general knowledge.

## Technology Stack

- Python
- LangChain
- Ollama
- Llama 3.2
- nomic-embed-text
- ChromaDB

## Workflow

1. Load `Documents/company_document.txt`
2. Split the document into 4 chunks
3. Generate embeddings
4. Store embeddings in ChromaDB
5. Retrieve the top 2 relevant chunks
6. Build the RAG context
7. Generate an answer with Llama 3.2

## Run

```bash
python rag_app.py
```

The application supports interactive questions and exits when the user enters `exit`.

## Testing

Six test scenarios were executed and all passed:

- Leave policy
- Working hours
- Work from home
- Salary
- IT support
- Unsupported maternity-policy query

Overall result: **6/6 passed (100%)**.
