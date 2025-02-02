from transformers import pipeline
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .models import Document
from .serializers import DocumentSerializer
from .utils.pdf_reader import PDFReader
from .utils.embeddings import EmbeddingGenerator
from .utils.retriever import Retriever
from .utils.reranker import Reranker
from .utils.prompt import Prompt

class LoadDocumentAPI(APIView):
    embedding_generator = EmbeddingGenerator()

    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "File is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Save file and extract text
        text = PDFReader.extract_text(file)

        # Generate embeddings
        embeddings = self.embedding_generator.generate_embeddings(text)

        # Save document with file, text, and embeddings
        document = Document(title=file.name, content=text, file=file)  # Save the file
        document.save_embeddings(embeddings)  # Save embeddings using the method from the model
        document.save()

        return Response({"message": "Document ingested successfully"}, status=status.HTTP_201_CREATED)



class QuestionAndAnswerAPI(APIView):
    embedding_generator = EmbeddingGenerator()

    def post(self, request):
        question = request.data.get('question')
        if not question:
            return Response({"error": "Question is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Generate query embeddings
        query_embedding = self.embedding_generator.generate_embeddings(question)
        # QuestionAndAnswerAPI
        print("Generated query embedding:", query_embedding)


        # Retrieve relevant documents
        documents = Document.objects.all()
        relevant_docs = Retriever.retrieve_relevant_documents(query_embedding, documents)

        # Check if relevant_docs is None or empty
        if not relevant_docs:
            return Response({"error": "No relevant document found"}, status=status.HTTP_404_NOT_FOUND)

        # Rerank documents only if relevant_docs is valid
        reranked_docs = Reranker.rerank_documents(question, relevant_docs)

        if reranked_docs:
            # Create the prompt and query the model
            prompt = Prompt.create_prompt(question, reranked_docs[0])
            context = reranked_docs[0].content 
            answer = self.query_model(question, context)
            return Response({"answer": answer}, status=status.HTTP_200_OK)

        return Response({"error": "No relevant document found after reranking"}, status=status.HTTP_404_NOT_FOUND)

    def query_model(self, question, context):
        model = pipeline("question-answering", model="deepset/roberta-base-squad2", token=settings.HUGGINGFACE_API_KEY)
        result = model({"context": context, "question": question})
        return result['answer']


  



