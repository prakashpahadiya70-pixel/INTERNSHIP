from dotenv import load_dotenv
import os

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env")

# 1. Load PDF
pdf_path = "uploads/company_policy.pdf"

loader = PyPDFLoader(pdf_path)
documents = loader.load()

print(f"📄 PDF loaded successfully!")
print(f"📑 Total pages: {len(documents)}")

# 2. Split PDF into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

print(f"🧩 Total chunks: {len(chunks)}")

# 3. Gemini Embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=api_key
)

# 4. Store chunks in ChromaDB
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="chroma_db"
)

print("✅ Documents stored in ChromaDB!")

# 5. Create Retriever
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

# 6. Test Retrieval
query = "How can an employee apply for leave?"

results = retriever.invoke(query)

print("\n🔎 Retrieved Results:\n")

for i, result in enumerate(results, 1):
    print(f"--- Result {i} ---")
    print(result.page_content)
    print()