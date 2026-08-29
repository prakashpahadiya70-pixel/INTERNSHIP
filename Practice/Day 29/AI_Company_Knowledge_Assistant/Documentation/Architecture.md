# AI Company Knowledge Assistant — Architecture

## Overview

The project uses a Retrieval-Augmented Generation (RAG) architecture to answer employee questions using company documentation.

## Data Flow

```text
Company Document
      |
      v
   TextLoader
      |
      v
Document Chunking
      |
      v
nomic-embed-text
      |
      v
   ChromaDB
      |
      | semantic retrieval
      v
  Relevant Chunks
      |
      v
   RAG Prompt
      |
      v
   Llama 3.2
      |
      v
  Grounded Answer
```

## Components

- **TextLoader:** loads the company text document.
- **RecursiveCharacterTextSplitter:** splits the document into smaller chunks.
- **nomic-embed-text:** creates vector embeddings.
- **ChromaDB:** stores and searches document embeddings.
- **Retriever:** returns the most relevant chunks for a question.
- **Llama 3.2:** generates the final natural-language answer.
- **RAG prompt:** instructs the model to use only the supplied company context.

## Important Design Decision

A fresh ChromaDB directory is created for each clean run so repeated execution does not accumulate duplicate chunks.
