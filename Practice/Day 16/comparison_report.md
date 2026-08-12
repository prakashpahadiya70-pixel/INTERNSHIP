# Day 16 - RAG Retrieval Performance Comparison Report

## 1. Objective

The objective of this experiment is to evaluate the performance of a basic Retrieval-Augmented Generation (RAG) system using different document chunk sizes.

The experiment compares chunk sizes of 200, 500, and 1000 and evaluates the quality of generated answers.

---

## 2. Company Documentation

A sample company employee documentation was used as the knowledge base.

The documentation contains information about:

- Company working hours
- Leave policy
- Work from home
- Attendance
- IT support
- HR support
- Salary
- Security policy
- Employee benefits

---

## 3. RAG Pipeline

The implemented RAG pipeline follows these steps:

Company Documentation
        ↓
Document Loading
        ↓
Text Chunking
        ↓
Embeddings
        ↓
ChromaDB Vector Database
        ↓
Semantic Retrieval
        ↓
Retrieved Context
        ↓
Llama 3.2
        ↓
Generated Answer

---

## 4. Embedding Model

The `nomic-embed-text` model was used to generate vector embeddings for the document chunks.

These embeddings were stored in ChromaDB for semantic search and retrieval.

---

## 5. LLM

Ollama with the Llama 3.2 model was used as the language model for generating answers from the retrieved company documentation.

---

## 6. Experimental Setup

Three different chunk configurations were tested.

| Experiment | Chunk Size | Chunk Overlap | Number of Chunks |
|---|---:|---:|---:|
| A | 200 | 20 | 11 |
| B | 500 | 50 | 4 |
| C | 1000 | 100 | 2 |

The same five questions were used for all three experiments.

---

## 7. Test Questions

1. How can an employee apply for leave?
2. What are the company working hours?
3. Who should I contact for technical problems?
4. Can employees work from home?
5. When are employee salaries processed?

---

## 8. Response Evaluation

Responses were evaluated on a scale of 1 to 5.

- 5 = Correct, complete and relevant
- 4 = Very good
- 3 = Good
- 2 = Partially correct
- 1 = Incorrect or irrelevant

### Evaluation Results

| Question | Chunk 200 | Chunk 500 | Chunk 1000 |
|---|---:|---:|---:|
| Leave application | 5 | 5 | 5 |
| Working hours | 5 | 5 | 5 |
| Technical problems | 5 | 5 | 5 |
| Work from home | 5 | 5 | 5 |
| Salary processing | 5 | 5 | 5 |
| **Average** | **5.0** | **5.0** | **5.0** |

---

## 9. Observations

### Chunk Size 200

The 200-size configuration generated 11 chunks.

The smaller chunks provided more granular information and produced accurate responses for all five questions.

### Chunk Size 500

The 500-size configuration generated 4 chunks.

It produced accurate and concise answers while maintaining sufficient context for the questions.

This configuration provided a good balance between context, retrieval efficiency and response quality.

### Chunk Size 1000

The 1000-size configuration generated only 2 chunks.

The larger chunks preserved more context and also produced accurate responses for all five questions. However, larger chunks may contain more information than necessary for a specific query.

---

## 10. Comparison

All three chunk sizes achieved an average response score of 5.0.

Therefore, response accuracy alone did not distinguish one configuration from another.

The main difference was the amount of information contained in each chunk.

- 200: More granular chunks
- 500: Balanced chunks
- 1000: Larger contextual chunks

---

## 11. Best Performing Configuration

The selected configuration is:

**Chunk Size = 500**

**Chunk Overlap = 50**

The 500-size configuration was selected because it provided a good balance between contextual information, retrieval efficiency and concise responses.

It also produced only 4 chunks compared with 11 chunks for the 200-size configuration, while maintaining the same response quality in this experiment.

---

## 12. Conclusion

The experiment demonstrated that document chunk size can affect the structure and efficiency of a RAG retrieval pipeline.

In this experiment, all three tested chunk sizes generated correct answers for the selected questions.

A chunk size of 500 with an overlap of 50 was selected as the preferred configuration because it provided a balanced trade-off between context and retrieval efficiency.

The experiment also demonstrated the complete RAG workflow using document loading, embeddings, ChromaDB, semantic retrieval and Llama 3.2.