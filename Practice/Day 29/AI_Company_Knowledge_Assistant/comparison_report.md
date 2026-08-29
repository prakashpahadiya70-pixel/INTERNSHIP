# RAG Chunking Comparison Report

## Purpose

Different chunk sizes were considered to understand their effect on retrieval.

| Chunk Size | General Observation |
|---:|---|
| 300 | Smaller context, more chunks |
| 500 | Balanced context and chunk count |
| 800 | Larger context, fewer chunks |

## Selected Configuration

The Day 29 implementation uses a moderate chunk size with overlap so related policy information remains together while retrieval remains focused.

The final clean test run produced **4 chunks** for the company document.
