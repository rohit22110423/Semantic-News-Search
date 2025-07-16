from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from model.news_fetcher import fetch_articles
from model.sbert_encoder import SBERTEncoder
from model.faiss_index import FAISSIndex

app = FastAPI()

encoder = SBERTEncoder()
index = FAISSIndex()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data once at startup
@app.on_event("startup")
def load_data():
    print("📥 Fetching news articles...")
    texts = fetch_articles(query="technology")
    if not texts:
        print("❌ No articles were fetched. Please check your NewsAPI key or query.")
        return
    embeddings = encoder.encode(texts)
    index.build(embeddings, texts)
    print(f"✅ Loaded {len(texts)} articles into the FAISS index.")

# Search endpoint
@app.get("/search")
def search(q: str = Query(...)):
    print(f"🔍 Searching for: {q}")
    q_vector = encoder.encode([q])[0]
    results = index.search(q_vector, k=5)
    formatted = []
    for text, score in results:
        snippet = text[:120].strip()
        print(f">>> Match Score: {round(score, 2)} | Snippet: {snippet}")
        formatted.append({"text": text, "score": round(score, 4)})

    return {"results": formatted}
