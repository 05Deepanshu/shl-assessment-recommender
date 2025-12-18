import requests
import json
import os
import uuid

API_URL = "https://www.shl.com/api/catalog/products"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.shl.com/solutions/products/product-catalog/",
    "Origin": "https://www.shl.com"
}

PARAMS = {
    "language": "en",
    "region": "global",
    "productType": "individual-test-solutions",
    "pageSize": 500
}

def scrape():
    os.makedirs("data/raw", exist_ok=True)

    res = requests.get(API_URL, headers=HEADERS, params=PARAMS, timeout=30)
    res.raise_for_status()

    products = res.json().get("products", [])

    data = []

    for p in products:
        data.append({
            "id": str(uuid.uuid4()),
            "name": p.get("name", ""),
            "url": "https://www.shl.com" + p.get("url", ""),
            "description": p.get("description", ""),
            "test_type": p.get("categories", []),
            "adaptive_support": "Yes" if p.get("adaptive") else "No",
            "remote_support": "Yes",
            "duration": p.get("duration", 0)
        })

    with open("data/raw/shl_catalog.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Scraped {len(data)} assessments")

if __name__ == "__main__":
    scrape()
