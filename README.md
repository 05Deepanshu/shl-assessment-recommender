SHL Assessment Recommender 🔍

A semantic search–based recommendation system that suggests the most relevant SHL assessments for a given job description using NLP embeddings and FAISS vector search.

Built with FastAPI, Sentence Transformers, and a modern UI, this project demonstrates end-to-end skills in data processing, machine learning, backend APIs, evaluation, and frontend integration.

- Features

 Semantic matching between job descriptions and SHL assessments

 NLP embeddings using sentence-transformers

 Fast similarity search with FAISS

 REST API built using FastAPI

 Evaluation using Recall@K

 Clean, modular project structure

 Project Architecture
shl-assessment-recommender/
│
├── backend/
│   ├── main.py           # FastAPI app
│   ├── recommender.py    # FAISS-based recommendation logic
│   ├── embeddings.py     # Embedding generation & indexing
│   ├── utils.py          # Text cleaning utilities
│   └── __init__.py
│
├── frontend/
│   ├── index.html        # UI
│   ├── styles.css        # Styling
│   └── app.js            # API integration
│
├── data/
│   └── raw/
│       └── shl_catalog.csv
│
├── vector_store/
│   ├── index.faiss
│   └── metadata.pkl
│
├── evaluation/
│   └── evaluate.py
│
├── requirements.txt
└── README.md

🧠 How It Works

Assessment Catalog

A curated dataset of 134 SHL assessments stored in CSV format.

Text Embeddings

Each assessment is converted into a vector using a Sentence Transformer model.

Vector Indexing

FAISS indexes these embeddings for fast similarity search.

Query Processing

A job description is embedded and compared against the index.

Recommendation

Top-K most similar assessments are returned via API and shown in the UI.

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/05deepanshu/shl-assessment-recommender.git
cd shl-assessment-recommender

2️⃣ Create & activate virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

- Generate Embeddings (One-time)
python backend/embeddings.py


This will create:

vector_store/index.faiss

vector_store/metadata.pkl

- Run the Backend API

uvicorn backend.main:app --reload


API Docs: http://127.0.0.1:8000/docs

Health Check: http://127.0.0.1:8000/health