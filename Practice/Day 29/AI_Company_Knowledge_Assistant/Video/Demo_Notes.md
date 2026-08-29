# Day 29 Video / Demo Notes

## Introduction
This project is an AI Company Knowledge Assistant based on Retrieval-Augmented Generation.

## Problem
Employees may need to search company information manually. The assistant provides a faster question-answering interface over company documentation.

## Architecture
Company document -> chunking -> embeddings -> ChromaDB -> retriever -> RAG prompt -> Llama 3.2 -> answer.

## Live Demo
Ask:
`How can an employee apply for leave?`

Expected:
`According to the company documentation, an employee can apply for leave through the HR portal.`

Then demonstrate an unsupported question:
`What is the company's maternity policy?`

Explain that the system should not fabricate information that is absent from the knowledge base.

## Testing
Six test cases were executed with 6/6 passing.

## Conclusion
The project demonstrates an end-to-end local RAG workflow with document processing, vector retrieval, grounded generation, and negative testing.
