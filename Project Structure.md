Semantic-News-Search/
│
├── backend/ # FastAPI backend with Sentence-BERT and FAISS
│ ├── main.py # Main API server with /search endpoint
│ ├── model/ # Sentence-BERT model loading and embedding
│ ├── data/ # CSV/JSON or preprocessed news data
│ ├── requirements.txt # Python dependencies
│ └── ...
│
├── frontend/ # React frontend using CRA (Create React App)
│ ├── public/
│ ├── src/
│ │ ├── components/ # React components (Header, NewsCard)
│ │ ├── App.jsx # Main app logic and layout
│ │ ├── api.js # Axios wrapper for /search API
│ │ └── index.jsx # Entry point
│ ├── package.json
│ └── ...
│
├── .gitignore # Files/folders to ignore in Git
├── LICENSE # MIT License
├── README.md # Project overview and instructions
└── project-structure.md # This file