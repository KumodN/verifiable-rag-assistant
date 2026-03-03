# 🏦 Secure Bank – Lending Policy AI Assistant

A local Retrieval-Augmented Generation (RAG) application that allows users to query Secure Bank Ltd.’s **Commercial Lending Guidelines (2026)** using **Llama 3.2**.

Unlike generic chatbots, this system provides **verifiable answers with exact policy citations**, ensuring regulatory compliance and eliminating hallucinations.

---

## 🎯 Purpose

This application enables:

- Internal staff to quickly retrieve SME loan eligibility rules
- Credit officers to verify lending thresholds and compliance
- Risk teams to validate credit score tiers and documentation requirements
- Auditors to confirm policy-based decision logic

All answers are strictly grounded in the official lending policy documents.

---

## 🛠️ Tech Stack

- **LLM:** Llama 3.2 (local via Ollama)
- **Embeddings:** mxbai-embed-large
- **Vector Database:** ChromaDB
- **Framework:** LangChain
- **User Interface:** Streamlit
- **Containerization:** Docker

---

## 🚀 Core Features

### ✅ Policy-Grounded Responses
Answers are generated strictly from Secure Bank’s official lending guidelines.

### 📄 Page-Level Citations
Each response includes:
- Source document reference
- Page number
- Exact text chunk used

### 🔒 100% Local Execution
- No external API calls
- No cloud processing
- Full data privacy

### 🛑 Hallucination Prevention
A strict system prompt ensures:
- Out-of-scope questions are rejected
- No speculative answers
- No fabricated policy clauses

---

## ⚙️ Installation (Local Setup)

### 1️⃣ Clone the Repository

git clone https://github.com/KumodN/verifiable-banking-rag.git
cd verifiable-banking-rag
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Pull Required Models

Make sure Ollama is running, then:

ollama pull llama3.2:3b
ollama pull mxbai-embed-large
4️⃣ Ingest the Lending Policy
python src/ingest.py
5️⃣ Launch the Application
streamlit run app.py
### 🐳 Docker Setup (Recommended)
Prerequisites

Docker Desktop installed

Ollama installed and running

Required models pulled:

llama3.2:3b

mxbai-embed-large

Build the Docker Image
docker build -t secure-bank-rag .
Run the Container
docker run -p 8501:8501 secure-bank-rag

Then open:

http://localhost:8501
### 🧠 Example Queries

“What is the maximum SME loan amount?”

“Are borrowers with a 640 credit score eligible?”

“What documents are required for loans above $100,000?”

“What is the DSCR requirement?”

“Can unsecured loans exceed $250,000?”

### 🛡️ Compliance & Governance

This system is designed for:

Internal policy interpretation only

Not a replacement for formal Credit Committee approval

Not legal advice

Not customer-facing production advice

All lending decisions must follow Secure Bank’s official approval workflow.

### 🔄 How It Works (High-Level Architecture)

Lending policy PDF is chunked and embedded

Chunks stored in ChromaDB

User query is embedded

Top-k relevant policy sections retrieved

Llama 3.2 generates response using only retrieved context

Source citation is displayed in UI

### 📌 Future Improvements

Multi-policy support (Credit Risk + AML + Collateral Policy)

Role-based access control

Audit logging of queries

Loan decision simulation mode

JSON API endpoint for internal systems

### 📜 License

Internal Secure Bank Project – 2026
Confidential – Not for external distribution
