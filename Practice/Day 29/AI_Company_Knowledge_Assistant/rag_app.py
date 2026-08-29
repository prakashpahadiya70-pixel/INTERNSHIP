from pathlib import Path
import shutil

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_chroma import Chroma

BASE_DIR = Path(__file__).resolve().parent
DOCUMENT_PATH = BASE_DIR / "Documents" / "company_document.txt"
CHROMA_DIR = BASE_DIR / "chroma_db"


def build_vectorstore():
    if CHROMA_DIR.exists():
        shutil.rmtree(CHROMA_DIR)

    loader = TextLoader(str(DOCUMENT_PATH), encoding="utf-8")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
    )
    chunks = splitter.split_documents(documents)

    for i, chunk in enumerate(chunks):
        chunk.metadata["chunk_id"] = f"day29_chunk_{i + 1}"

    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    vectorstore = Chroma(
        collection_name="company_docs_day29",
        embedding_function=embeddings,
        persist_directory=str(CHROMA_DIR),
    )
    vectorstore.add_documents(
        documents=chunks,
        ids=[chunk.metadata["chunk_id"] for chunk in chunks],
    )

    return vectorstore, chunks


def answer_question(question, retriever, llm):
    retrieved = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in retrieved)

    prompt = f"""You are an AI Company Knowledge Assistant.

Answer the user's question using ONLY the company documentation provided below.
If the documentation does not contain the answer, clearly say that the information
is not available in the provided company documentation. Do not invent policies.

Company documentation:
{context}

User question:
{question}

Answer:"""

    response = llm.invoke(prompt)
    return response.content, retrieved


def main():
    print("=" * 60)
    print("       AI COMPANY KNOWLEDGE ASSISTANT")
    print("=" * 60)

    print("\n[1] Loading company documentation...")
    vectorstore, chunks = build_vectorstore()
    print("Document loaded and indexed successfully!")
    print(f"Number of chunks: {len(chunks)}")

    print("\n[2] Creating retriever...")
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
    print("Retriever created successfully!")

    print("\n[3] Initializing Llama 3.2...")
    llm = ChatOllama(model="llama3.2", temperature=0)
    print("Llama 3.2 initialized successfully!")

    print("\nType 'exit' to quit.")

    while True:
        question = input("\nAsk your question: ").strip()

        if question.lower() == "exit":
            print("Goodbye!")
            break

        if not question:
            print("Please enter a question.")
            continue

        print("\nRetrieved context:")
        answer, retrieved = answer_question(question, retriever, llm)

        for i, doc in enumerate(retrieved, 1):
            print(f"\n--- Retrieved Chunk {i} ---")
            print(doc.page_content)

        print("\n" + "=" * 60)
        print("AI ANSWER")
        print("=" * 60)
        print(answer)


if __name__ == "__main__":
    main()
