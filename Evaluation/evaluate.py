import sys
import os
sys.path.append(os.path.abspath("."))

import pandas as pd
from backend.recommender import recommend

df = pd.read_excel("Gen_AI Dataset.xlsx")

correct = 0
total = 0

for _, row in df.iterrows():
    query = row["Query"]
    expected = row["Correct Assessment"]

    results = recommend(query, top_k=10)
    names = [r["Assessment Name"] for r in results]

    if expected in names:
        correct += 1

    total += 1

recall_at_10 = correct / total if total > 0 else 0
print(f"Recall@10: {recall_at_10:.2f}")
