# Day 29 Demo Practice Checklist

## Before Demo
- [ ] Start Ollama
- [ ] Confirm `llama3.2` is available
- [ ] Confirm `nomic-embed-text` is available
- [ ] Activate the virtual environment
- [ ] Run `python rag_app.py`

## Positive Demo
Question:
> How can an employee apply for leave?

Expected answer:
The employee can apply for leave through the HR portal.

## Negative Demo
Question:
> What is the company's maternity policy?

Expected behavior:
The assistant should not invent an answer when the information is not present in the company documentation.

## Explain During Demo
1. Document loading
2. Chunking
3. Embedding generation
4. ChromaDB storage
5. Retrieval
6. RAG prompt
7. Llama 3.2 response
8. Grounded/fallback behavior
