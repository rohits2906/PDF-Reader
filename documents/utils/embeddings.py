# documents/utils/embeddings.py
from sentence_transformers import SentenceTransformer
import numpy as np

class EmbeddingGenerator:
    def __init__(self):
        # Load a pre-trained SentenceTransformer model
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def generate_embeddings(self, text):
        """
        Generate embeddings for a given text (string).
        """
        embeddings = self.model.encode(text)
        return embeddings  # Returns a 1D array of embeddings
