from django.test import TestCase
from documents.models import Document
import numpy as np

class DocumentModelTest(TestCase):

    def test_save_embeddings(self):
        embeddings = np.array([1.2, 3.4, 5.6], dtype=np.float32)
        document = Document(title="Test", content="Test content")
        document.save_embeddings(embeddings)

        # Check if embeddings are saved correctly
        self.assertEqual(document.embeddings, embeddings.tobytes())
        self.assertEqual(document.embeddings_shape, str(embeddings.shape))

    def test_get_embeddings(self):
        embeddings = np.array([1.2, 3.4, 5.6], dtype=np.float32)
        document = Document(title="Test", content="Test content")
        document.save_embeddings(embeddings)

        # Retrieve embeddings and check if they match the original
        retrieved_embeddings = document.get_embeddings()
        np.testing.assert_array_equal(retrieved_embeddings, embeddings)
