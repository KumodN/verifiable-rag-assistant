import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

DB_PATH = "chroma_db"
EMBEDDING_MODEL = "mxbai-embed-large"
CHAT_MODEL = "llama3.2:3b"

embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
vector_db = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)

retriever = vector_db.as_retriever(search_kwargs={"k": 3})

template = """
You are a helpful assistant.
Answer the question based ONLY on the following context. 
If the answer is not in the context, say "I don't know."

Context:
{context}

Question:
{question}
"""

prompt = ChatPromptTemplate.from_template(template)
llm = ChatOllama(model=CHAT_MODEL)

def query_rag(question_text):
    results = retriever.invoke(question_text)
    context_text = "\n\n".join([doc.page_content for doc in results])
    chain = prompt | llm
    response = chain.invoke({"context": context_text, "question": question_text})
    
    return {
        "answer": response.content,
        "sources": results
    }

# TEST IT
if __name__ == "__main__":
    print("--- Testing Llama 3.2 RAG ---")
    response = query_rag("What is this document about?")
    print(f"Answer: {response['answer']}")