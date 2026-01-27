import requests
import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# 1. NEW TOOL: CALL BANKING API
def check_client_eligibility(client_id):
    """
    Connects to the Core Banking System.
    Fetches client credit score and compares against known rules.
    """
    try:
        response = requests.get(f"http://localhost:8000/client/{client_id}")
        if response.status_code == 200:
            data = response.json()
            score = data['credit_score']
            name = data['name']
            
            # Simple Logic (You could also let the AI decide this)
            status = "APPROVED" if score >= 650 else "REJECTED"
            
            return f"🔒 **SECURE LOOKUP RESULT:**\n" \
                   f"Client: {name}\n" \
                   f"Credit Score: {score}\n" \
                   f"System Status: {status} (Threshold is 650)"
        else:
            return "❌ Client ID not found in Core Banking System."
    except:
        return "⚠️ Error: Core Banking System is offline."

DB_PATH = "chroma_db"
EMBEDDING_MODEL = "mxbai-embed-large"
CHAT_MODEL = "llama3.2:3b"
OLLAMA_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL, base_url=OLLAMA_URL)
vector_db = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)

retriever = vector_db.as_retriever(search_kwargs={"k": 3})

template = """
You are "Vault", a Security & Compliance AI for Secure Bank Ltd.
Your job is to assist Loan Officers by retrieving strict policy rules.

SECURITY PROTOCOLS:
1. This is a SECURE environment. Do not share data externally.
2. Answer based ONLY on the Lending Guidelines context.
3. If the answer is not in the guidelines, state: "Policy not found in current documentation."
4. Be precise with numbers (Interest rates, eligibility criteria).

CONTEXT:
{context}

QUERY:
{question}
"""

prompt = ChatPromptTemplate.from_template(template)
llm = ChatOllama(model=CHAT_MODEL, base_url=OLLAMA_URL, temperature=0)

# 3. UPDATED ROUTER
def query_rag(question_text):
    
    # TRIGGER: Checking a specific client ID
    # Example: "Is client C101 eligible?"
    if "client" in question_text.lower() and any(char.isdigit() for char in question_text):
        # Extract the ID (Simple hack for demo: finds 'C101' etc)
        words = question_text.split()
        client_id = next((w for w in words if w.startswith("C") and w[1:].isdigit()), "C101")
        
        print(f"🔐 Secure Routing to Banking API for: {client_id}")
        return {
            "answer": check_client_eligibility(client_id),
            "sources": []
        }
    
    # ELSE: Policy Question
    results = retriever.invoke(question_text)
    context_text = "\n\n".join([doc.page_content for doc in results])
    chain = prompt | llm
    response = chain.invoke({"context": context_text, "question": question_text})
    
    return {
        "answer": response.content,
        "sources": results
    }