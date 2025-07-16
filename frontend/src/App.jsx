import React, { useState } from 'react';
import axios from 'axios';
import './App.css';
import NewsCard from './components/NewsCard';

function App() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    if (!query.trim()) return;

    setLoading(true);
    try {
      const response = await axios.get(`http://localhost:8000/search?q=${query}`);
      setResults(response.data.results);
    } catch (error) {
      console.error('Error fetching results:', error);
      setResults([]);
    }
    setLoading(false);
  };

  return (
    <div className="app-container">
      <header className="header">
        <h1>Semantic News Search</h1>
      </header>

      <div className="search-bar">
        <input
          type="text"
          placeholder="Search news articles..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && handleSearch()}
        />
        <button onClick={handleSearch}>🔍</button>
      </div>

      {loading ? (
        <div className="loading">Loading...</div>
      ) : (
        <div className="results">
          {results.map((item, index) => (
            <NewsCard key={index} score={item.score} text={item.text} />
          ))}
        </div>
      )}
    </div>
  );
}

export default App;
