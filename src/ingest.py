import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

# 1. SETTINGS
PDF_PATH = "data/KUMOD DE SILVA Resume.pdf"
DB_PATH = "chroma_db"

def ingest_docs():
    print("--- 1. Loading PDF ---")
    if not os.path.exists(PDF_PATH):
        print(f"Error: File {PDF_PATH} not found.")
        return

    loader = PyPDFLoader(PDF_PATH)
    raw_documents = loader.load()
    print(f"Loaded {len(raw_documents)} pages.")

    print("--- 2. Splitting Text ---")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80
    )
    chunks = text_splitter.split_documents(raw_documents)
    print(f"Split into {len(chunks)} chunks.")

    print("--- 3. Creating Embeddings ---")
    embeddings = OllamaEmbeddings(model="mxbai-embed-large")

    print("--- 4. Saving to Vector DB ---")
    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_PATH
    )
    print("--- DONE! Database created in folder 'chroma_db' ---")

if __name__ == "__main__":
    ingest_docs()