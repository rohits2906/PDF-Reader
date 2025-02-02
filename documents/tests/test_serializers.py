from django.test import TestCase
from rest_framework.exceptions import ValidationError
from documents.serializers import DocumentSerializer
from documents.models import Document

class DocumentSerializerTest(TestCase):

    def test_valid_serializer(self):
        document = Document.objects.create(title="Test", content="Test content")
        serializer = DocumentSerializer(document)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.data['title'], document.title)

    def test_invalid_serializer(self):
        # Test case where required field is missing
        data = {'content': 'Test content'}
        serializer = DocumentSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)
