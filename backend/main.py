from fastapi import FastAPI
from pydantic import BaseModel
from backend.recommender import recommend

app = FastAPI(title="SHL Assessment Recommender")

class QueryRequest(BaseModel):
    query: str
    top_k: int = 10

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/recommend")
def recommend_assessments(req: QueryRequest):
    results = recommend(req.query, req.top_k)
    return {"recommendations": results}
