from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma


# 1. Load company documentation
loader = TextLoader(
    "documents/company_document.txt",
    encoding="utf-8"
)

documents = loader.load()

print("Document loaded successfully!")
print("Number of documents:", len(documents))


# 2. Split document into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)

print("Document split successfully!")
print("Number of chunks:", len(chunks))


# 3. Display chunks
for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i + 1} ---")
    print(chunk.page_content)


# 4. Create embeddings
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)
print("\nEmbeddings model initialized successfully!")


# 5. Create ChromaDB vector store
vectorstore = Chroma(
    collection_name="company_documents",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)


# 6. Store document chunks in ChromaDB
vectorstore.add_documents(chunks)

print("Documents added to ChromaDB successfully!")
print("Total chunks stored:", len(chunks))


# 7. Create retriever
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

print("\nRetriever created successfully!")


# 8. Test retrieval
question = "How can an employee apply for leave?"

retrieved_docs = retriever.invoke(question)

print("\nQuestion:")
print(question)

print("\nRetrieved Documents:")

for i, doc in enumerate(retrieved_docs):
    print(f"\n--- Retrieved Chunk {i + 1} ---")
    print(doc.page_content)


from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


# 9. Create Llama 3.2 LLM
llm = OllamaLLM(
    model="llama3.2"
)

print("\nLlama 3.2 initialized successfully!")


# 10. Create RAG prompt
prompt = ChatPromptTemplate.from_template("""
You are a helpful company support assistant.

Answer the user's question using ONLY the provided company documentation.

If the answer is not available in the documentation, say:
"I don't have that information in the provided company documentation."

Do not make up information.

Company Documentation:
{context}

User Question:
{question}

Answer:
""")


# 11. Generate answer using retrieved documents
context = "\n\n".join(
    doc.page_content for doc in retrieved_docs
)

final_prompt = prompt.format(
    context=context,
    question=question
)

print("\nGenerating AI answer...")

answer = llm.invoke(final_prompt)

print("\n========== AI ANSWER ==========")
print(answer)
print("================================")
