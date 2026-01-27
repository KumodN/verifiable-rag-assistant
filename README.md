# 🤖 Verifiable AI Research Assistant

A local RAG (Retrieval-Augmented Generation) application that allows users to chat with PDF documents using **Llama 3.2**. 

Unlike standard chatbots, this system prevents hallucinations by using a "Grounding Prompt" and provides **verifiable page citations** for every answer.

## 🛠️ Tech Stack
* **LLM:** Llama 3.2 (running locally via Ollama)
* **Embeddings:** mxbai-embed-large
* **Vector DB:** ChromaDB
* **Orchestration:** LangChain
* **UI:** Streamlit

## 🚀 Features
* **100% Local Privacy:** No data leaves the machine.
* **Citation Verification:** The UI expands to show the exact page number and text chunk used for the answer.
* **Hallucination Mitigation:** Uses a strict system prompt to reject questions outside the document scope.

## 💻 Installation
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run the ingestion script: `python src/ingest.py`
4. Launch the app: `python -m streamlit run app.py`

## 🐳 How to Run (Docker Way)
This is the recommended way to run the application to ensure all dependencies are isolated.

### Prerequisites
1. **Docker Desktop** installed and running.
2. **Ollama** installed and running.
   * *Required Models:* Run `ollama pull llama3.2:3b` and `ollama pull mxbai-embed-large` in your terminal first.

### Quick Start
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/verifiable-rag-assistant.git](https://github.com/YOUR_USERNAME/verifiable-rag-assistant.git)
   cd verifiable-rag-assistant
