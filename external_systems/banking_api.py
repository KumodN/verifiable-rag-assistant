# external_systems/banking_api.py
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Core Banking Simulator")

# MOCK CLIENT DATABASE (Sensitive Data - Local Only!)
clients_db = {
    "C101": {
        "name": "TechStart Solutions",
        "type": "SME",
        "credit_score": 780,
        "operational_years": 3
    },
    "C102": {
        "name": "Bakery Bros",
        "type": "SME",
        "credit_score": 620, # Low Score
        "operational_years": 5
    }
}

@app.get("/")
def home():
    return {"status": "Secure Core Banking Online 🔒"}

@app.get("/client/{client_id}")
def get_client_financials(client_id: str):
    """Fetch sensitive client financial data"""
    if client_id in clients_db:
        return clients_db[client_id]
    raise HTTPException(status_code=404, detail="Client ID not found")