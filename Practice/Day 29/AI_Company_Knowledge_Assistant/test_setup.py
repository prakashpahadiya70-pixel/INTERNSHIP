from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

print("LangChain setup successful!")

embeddings = OllamaEmbeddings(model="nomic-embed-text")
print("Ollama embeddings initialized successfully!")

vectorstore = Chroma(
    collection_name="setup_test",
    embedding_function=embeddings,
    persist_directory="./chroma_db",
)
print("ChromaDB initialized successfully!")
