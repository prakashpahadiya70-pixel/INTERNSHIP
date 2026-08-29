from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

document = Path("Documents/company_document.txt")

loader = TextLoader(str(document), encoding="utf-8")
docs = loader.load()

print("Loaded documents:", len(docs))

for size in [300, 500, 800]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=size,
        chunk_overlap=50,
    )
    chunks = splitter.split_documents(docs)
    print(f"chunk_size={size}: {len(chunks)} chunks")
