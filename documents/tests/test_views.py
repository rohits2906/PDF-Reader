from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from documents.models import Document
from unittest.mock import patch

class LoadDocumentAPITest(APITestCase):

    def test_document_upload(self):
        url = reverse('document-ingestion')  # Replace with your actual URL name
        with open('path_to_test_pdf.pdf', 'rb') as pdf_file:
            data = {'file': pdf_file}
            response = self.client.post(url, data, format='multipart')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(response.data['message'], "Document ingested successfully")

class QuestionAndAnswerAPIUnitTest(APITestCase):

    @patch('documents.views.Retriever.retrieve_relevant_documents')
    def test_qa_post(self, mock_retrieve):
        # Mock the response of the Retriever
        mock_retrieve.return_value = [Document.objects.first()]  # Simulate that relevant docs were found

        url = reverse('qa-api')  # Replace with the correct URL name
        data = {"question": "What is this document about?"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('answer', response.data)
