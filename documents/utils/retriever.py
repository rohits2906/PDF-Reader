from sklearn.metrics.pairwise import cosine_similarity

from sklearn.metrics.pairwise import cosine_similarity

class Retriever:
    @staticmethod
    def retrieve_relevant_documents(query_embedding, documents):
        similarities = []
        for doc in documents:
            doc_embedding = doc.get_embeddings()
            similarity = cosine_similarity([query_embedding], [doc_embedding])[0][0]
            similarities.append((doc, similarity))

        # Sort documents by similarity score (highest first)
        sorted_docs = sorted(similarities, key=lambda x: x[1], reverse=True)

        # Return top N documents based on similarity
        return [doc for doc, _ in sorted_docs[:5]]  # Adjust N as needed,here N= 5
