from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.recommender import recommend

app = FastAPI(title="SHL Assessment Recommender")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RecommendRequest(BaseModel):
    query: str
    top_k: int = 5

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/recommend")
def recommend_assessments(req: RecommendRequest):
    return recommend(req.query, req.top_k)
