# Semantic News Search 🔍📰

**A full-stack semantic news search application using FastAPI, Sentence-BERT, FAISS, and React.**

---

## 🚀 Features
- Semantic search over news articles using SBERT + FAISS
- FastAPI backend with `/search` endpoint
- Modern React frontend with real-time results and responsive UI
- Match score & snippet display
- Loading indicator and mobile-friendly layout

---

## 🛠 Tech Stack
- **Backend**: FastAPI, Python, FAISS, Sentence-BERT
- **Frontend**: React (`create-react-app`), CSS
- **Deployment**: Ready for GitHub Pages / Vercel / Netlify and PythonAnywhere / Railway

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/rohit22110423/Semantic-News-Search.git
cd Semantic-News-Search


cd backend
pip install -r requirements.txt
# Create a .env file with your NEWSAPI_KEY
uvicorn main:app --reload


cd frontend
npm install
npm start
