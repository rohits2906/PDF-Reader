from django.urls import resolve,reverse
from documents.views import LoadDocumentAPI, QuestionAndAnswerAPI
from django.test import TestCase

class TestURLs(TestCase):

    def test_document_ingestion_url(self):
        url = reverse('document-ingestion')  # Replace with actual URL name
        resolved = resolve(url)
        self.assertEqual(resolved.view_name, 'document-ingestion')
        self.assertEqual(resolved.func.view_class, LoadDocumentAPI)

    def test_qa_api_url(self):
        url = reverse('qa-api')  # Replace with actual URL name
        resolved = resolve(url)
        self.assertEqual(resolved.view_name, 'qa-api')
        self.assertEqual(resolved.func.view_class, QuestionAndAnswerAPI)
