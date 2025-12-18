import pandas as pd
import faiss
import pickle
import os
from sentence_transformers import SentenceTransformer

df = pd.read_csv("data/raw/shl_catalog.csv")

if df.empty:
    raise RuntimeError("Catalog is empty")

texts = (
    df["name"].astype(str)
    + " "
    + df["description"].astype(str)
).tolist()

metadata = df.to_dict(orient="records")

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(texts, show_progress_bar=True)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

os.makedirs("vector_store", exist_ok=True)
faiss.write_index(index, "vector_store/index.faiss")

with open("vector_store/metadata.pkl", "wb") as f:
    pickle.dump(metadata, f)

print(f"Embedded {len(metadata)} assessments")
