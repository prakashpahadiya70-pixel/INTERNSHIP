from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader


KNOWLEDGE_FILE = Path(__file__).parent.parent / "data" / "company_knowledge.txt"

def load_and_split_documents():
    """
    Load the company knowledge document and split it into smaller chunks.

    Returns:
        list: Document chunks ready for embedding and retrieval.
    """
    if not KNOWLEDGE_FILE.exists():
        raise FileNotFoundError(
            f"Knowledge base file not found: {KNOWLEDGE_FILE}"
        )

    loader = TextLoader(str(KNOWLEDGE_FILE), encoding="utf-8")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    return splitter.split_documents(documents)