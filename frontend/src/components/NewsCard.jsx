import React from 'react';
import './NewsCard.css';

function NewsCard({ score, text }) {
  return (
    <div className="news-card">
      <div className="score">Match Score: {score.toFixed(2)}</div>
      <div className="snippet">{text}</div>
    </div>
  );
}

export default NewsCard;
