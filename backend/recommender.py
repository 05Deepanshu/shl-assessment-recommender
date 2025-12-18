import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

INDEX_PATH = "vector_store/index.faiss"
META_PATH = "vector_store/metadata.pkl"

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index(INDEX_PATH)

with open(META_PATH, "rb") as f:
    metadata = pickle.load(f)

def recommend(query: str, top_k: int = 10):
    query_vec = model.encode([query])
    distances, indices = index.search(np.array(query_vec), top_k * 3)

    results = []
    seen_types = set()

    for idx in indices[0]:
        item = metadata[idx]
        test_type = item.get("test_type", "Unknown")

        if test_type not in seen_types or len(results) < top_k:
            results.append(item)
            seen_types.add(test_type)

        if len(results) >= top_k:
            break

    return results
