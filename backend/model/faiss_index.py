import faiss
import numpy as np

class FAISSIndex:
    def __init__(self):
        self.index = None
        self.texts = []

    def build(self, embeddings, texts):
        self.texts = texts
        d = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(d)
        self.index.add(embeddings)

    def search(self, query_vector, k=5):
        if self.index is None:
            return []
        distances, indices = self.index.search(np.array([query_vector]), k)
        results = []
        for idx, dist in zip(indices[0], distances[0]):
            if idx < len(self.texts):
                results.append((self.texts[idx], float(dist)))
        return results
