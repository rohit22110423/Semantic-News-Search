// src/api.js
import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8000';

export const searchNews = async (query) => {
  try {
    const response = await axios.get(`${BASE_URL}/search?q=${query}`);
    return response.data.results || [];
  } catch (error) {
    console.error('Search failed:', error);
    return [];
  }
};
