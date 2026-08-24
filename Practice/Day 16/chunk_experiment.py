from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import OllamaLLM
import shutil
import os


# Load document
loader = TextLoader(
    "documents/company_document.txt",
    encoding="utf-8"
)

documents = loader.load()


# Embedding model
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)


# LLM
llm = OllamaLLM(
    model="llama3.2"
)


# Test questions
questions = [
    "How can an employee apply for leave?",
    "What are the company working hours?",
    "Who should I contact for technical problems?",
    "Can employees work from home?",
    "When are employee salaries processed?"
]


# Chunk size experiments
experiments = [
    (200, 20),
    (500, 50),
    (1000, 100)
]


for chunk_size, chunk_overlap in experiments:

    print("\n" + "=" * 60)
    print(f"CHUNK SIZE: {chunk_size}")
    print(f"CHUNK OVERLAP: {chunk_overlap}")
    print("=" * 60)

    # Create chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = text_splitter.split_documents(documents)

    print(f"Number of chunks: {len(chunks)}")

    # Unique ChromaDB directory for each experiment
    db_path = f"./chroma_experiment_{chunk_size}"

    if os.path.exists(db_path):
        shutil.rmtree(db_path)

    vectorstore = Chroma(
        collection_name=f"company_docs_{chunk_size}",
        embedding_function=embeddings,
        persist_directory=db_path
    )

    vectorstore.add_documents(chunks)

    # Retriever
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    # Test each question
    for question in questions:

        retrieved_docs = retriever.invoke(question)

        context = "\n\n".join(
            doc.page_content
            for doc in retrieved_docs
        )

        prompt = f"""
You are a helpful company support assistant.

Answer the question using ONLY the provided company documentation.

If the information is not available, say:
"I don't have that information in the provided company documentation."

Company Documentation:
{context}

Question:
{question}

Answer:
"""

        answer = llm.invoke(prompt)

        print("\nQuestion:", question)
        print("Answer:", answer)

    print("\nExperiment completed.")