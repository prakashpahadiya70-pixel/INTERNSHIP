from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

print("LangChain setup successful!")

embeddings = OllamaEmbeddings(model="llama3.2")

print("Ollama embeddings initialized successfully!")

vectorstore = Chroma(
    collection_name="company_docs",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)

print("ChromaDB initialized successfully!")