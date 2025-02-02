class Reranker:
    @staticmethod
    def rerank_documents(query, documents):
        if not documents:
            return []  # Return an empty list if no documents are provided
        
        # Ensure each document has the content attribute before accessing it
        valid_docs = [doc for doc in documents if hasattr(doc, 'content')]

        # If no valid documents found, return an empty list
        if not valid_docs:
            return []

        return sorted(valid_docs, key=lambda doc: len(doc.content), reverse=True)

