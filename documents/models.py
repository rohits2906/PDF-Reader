from django.db import models
import numpy as np

class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    embeddings = models.BinaryField()  # Store embeddings as binary data (bytes)
    embeddings_shape = models.CharField(max_length=255)  # Store the shape of the embeddings
    file = models.FileField(upload_to='documents/')  # Add this line to store uploaded files

    def save_embeddings(self, embeddings):
        """
        Save embeddings as bytes into the database along with their shape.
        :param embeddings: Embeddings as numpy array
        """
        self.embeddings = np.array(embeddings).tobytes()  # Convert embeddings to bytes
        self.embeddings_shape = str(embeddings.shape)  # Save the shape as a string
        self.save()

    def get_embeddings(self):
        """
        Retrieve embeddings from the database, reshape, and convert them back into numpy array.
        :return: Embeddings as numpy array
        """
        shape = eval(self.embeddings_shape)  # Convert the shape back to a tuple
        embeddings = np.frombuffer(self.embeddings, dtype=np.float32)
        return embeddings.reshape(shape)  # Reshape the embeddings to their original shape

