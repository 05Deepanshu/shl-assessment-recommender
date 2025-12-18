import sys
import os
sys.path.append(os.path.abspath("."))

import pandas as pd
from backend.recommender import recommend

df = pd.read_excel("Gen_AI Dataset.xlsx")

predictions = []

for idx, row in df.iterrows():
    query = row["Query"] if "Query" in df.columns else row[0]

    results = recommend(query, top_k=1)

    # SAFETY CHECK
    if not results:
        predicted_assessment = "No recommendation"
    else:
        predicted_assessment = results[0]["assessment"]

    predictions.append({
        "query": query,
        "predicted_assessment": predicted_assessment
    })

output_df = pd.DataFrame(predictions)
output_df.to_csv("deepanshu_katariya.csv", index=False)

print("Prediction file generated: deepanshu_katariya.csv")
