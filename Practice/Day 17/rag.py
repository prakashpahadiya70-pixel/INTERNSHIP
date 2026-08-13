import os

from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI


# Load environment variables
load_dotenv()


# -----------------------------
# Paths
# -----------------------------

UPLOAD_DIR = "uploads"
DB_DIR = "chroma_db"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(DB_DIR, exist_ok=True)


# -----------------------------
# Hugging Face Embeddings
# -----------------------------

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# -----------------------------
# Gemini LLM
# -----------------------------

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite"
)


# -----------------------------
# Process PDF
# -----------------------------

def process_pdf(pdf_path, file_name):

    # Load PDF
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    if not documents:
        raise ValueError("PDF contains no readable pages.")

    # Chunking
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    if not chunks:
        raise ValueError("PDF contains no readable text.")

    # Add metadata
    for chunk in chunks:
        chunk.metadata["source"] = file_name
        chunk.metadata["file_type"] = "pdf"

    # Store in ChromaDB
    vector_db = Chroma(
        collection_name="rag_documents",
        embedding_function=embedding_model,
        persist_directory=DB_DIR
    )

    vector_db.add_documents(chunks)

    return {
        "file_name": file_name,
        "pages": len(documents),
        "chunks": len(chunks)
    }


# -----------------------------
# Search Documents
# -----------------------------

def search_documents(question):

    vector_db = Chroma(
        collection_name="rag_documents",
        embedding_function=embedding_model,
        persist_directory=DB_DIR
    )

    results = vector_db.similarity_search(
        question,
        k=4
    )

    return results


# -----------------------------
# Generate Answer
# -----------------------------

def generate_answer(question):

    results = search_documents(question)

    if not results:
        return {
            "answer": "I could not find relevant information in the uploaded document.",
            "sources": []
        }

    # Combine retrieved chunks
    context = "\n\n".join(
        doc.page_content for doc in results
    )

    # Prompt
    prompt = f"""
You are a helpful company document assistant.

Answer the user's question using ONLY the information
provided in the context below.

If the answer is not present in the context, say:

"I could not find this information in the uploaded document."

Context:
{context}

Question:
{question}

Answer:
"""

    # Generate response
    response = llm.invoke(prompt)

    # Convert Gemini response to clean text
    answer_text = response.content

    if isinstance(answer_text, list):
        answer_text = "".join(
            item.get("text", "")
            for item in answer_text
            if isinstance(item, dict)
        )

    answer_text = answer_text.strip()

    # Remove duplicate sources
    sources = []
    seen_sources = set()

    for doc in results:

        source = doc.metadata.get("source")
        page = doc.metadata.get("page")

        source_key = (source, page)

        if source_key not in seen_sources:

            sources.append({
                "source": source,
                "page": page
            })

            seen_sources.add(source_key)

    return {
        "answer": answer_text,
        "sources": sources
    }