from pathlib import Path

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from knowledge_base import load_and_split_documents


CHROMA_DIR = Path(__file__).parent.parent / "chroma_db"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
COLLECTION_NAME = "company_support_knowledge"

RELEVANCE_THRESHOLD = 0.75


def get_embeddings():
    """Create the embedding model used by the vector database."""
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )


def create_vector_store():
    """
    Create the vector store from the company knowledge base.

    Returns:
        Chroma: Initialized vector store.
    """
    documents = load_and_split_documents()
    embeddings = get_embeddings()

    return Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=str(CHROMA_DIR),
        collection_name=COLLECTION_NAME
    )


def get_vector_store():
    """
    Load the existing vector store or create it if it does not exist.

    Returns:
        Chroma: Vector store ready for similarity search.
    """
    embeddings = get_embeddings()

    if CHROMA_DIR.exists():
        return Chroma(
            persist_directory=str(CHROMA_DIR),
            embedding_function=embeddings,
            collection_name=COLLECTION_NAME
        )

    return create_vector_store()


def retrieve_relevant_documents(query, k=3):
    """
    Retrieve documents that meet the configured relevance threshold.

    Args:
        query (str): Customer's natural-language question.
        k (int): Maximum number of documents to retrieve.

    Returns:
        list: Relevant documents with sufficient similarity.
    """
    if not query or not query.strip():
        return []

    vector_store = get_vector_store()

    results = vector_store.similarity_search_with_score(
        query.strip(),
        k=k
    )

    return [
        document
        for document, score in results
        if score <= RELEVANCE_THRESHOLD
    ]