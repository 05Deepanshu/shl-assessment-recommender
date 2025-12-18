import sys
import os
sys.path.append(os.path.abspath("."))

import pandas as pd
from backend.recommender import recommend


test_df = pd.read_excel("Gen_AI Dataset.xlsx")

predictions = []

for _, row in test_df.iterrows():
    query = row.iloc[0]  

    results = recommend(query, top_k=1)

    if results:
        
        predicted = (
            results[0].get("name")
            or results[0].get("assessment")
            or results[0].get("Assessment Name")
            or "Unknown"
        )
    else:
        predicted = "Unknown"

    predictions.append({
        "query": query,
        "predicted_assessment": predicted
    })


output_path = "deepanshu_katariya.csv"
pd.DataFrame(predictions).to_csv(output_path, index=False)

print(f"Prediction file generated: {output_path}")
