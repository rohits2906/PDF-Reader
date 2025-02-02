## RAG-Based Document Management and Q&A Application

### 1. **Overview**

The **RAG-Based Document Management and Q&A Application** is designed to manage documents and provide answers to user queries based on the document content. The solution utilizes **Django** for backend services and **Hugging Face's Transformers** for document processing.

### 2. **Components**

- **Document Upload**: Users can upload PDF documents. The document content is extracted and stored in a model, along with its embeddings (calculated using a transformer model).
- **Embeddings**: The application calculates embeddings of document content using models such as `deepset/roberta-base-squad2` and stores them in the database. These embeddings are used for retrieving relevant information during query processing.
- **Question Answering**: When a user submits a question, the application uses RAG to find the most relevant part of the document and generates an answer based on the context.
- **Modeling**: The model's `Document` class handles both the content storage and the embeddings associated with each document.
- **Testing**: The application includes unit tests for models, views, and APIs to ensure reliability.

### 3. **Architecture Flow**

1. **Document Upload**: When a PDF file is uploaded via the `/api/upload/` endpoint , the pdf is saved under the media folder then the system reads the document, extracts text, and calculates embeddings.
2. **Embedding Storage**: The embeddings are stored in a Django model (`Document`) along with the document's content and metadata.
3. **Querying**: A user sends a question via the `/api/qa/` endpoint. The application retrieves the most relevant document using RAG, passes the context along with the question to the Hugging Face model, and returns the generated answer.

### 4. **Libraries and Technologies**

- **Django**: The backend framework used to handle the web server, API, and database models.
- **Django Rest Framework (DRF)**: A powerful toolkit for building APIs in Django, used to create the endpoints for document upload and querying.
- **Hugging Face Transformers**: A deep learning library that powers the RAG functionality and is used to process and understand text.
- **Pypdf**: A library for reading and processing PDF documents.

### 5. **Database Schema**

The `Document` model consists of the following fields:

- `title`: The title of the document (e.g., file name or custom title).
- `content`: The full text content of the document.
- `embeddings`: The document's embeddings stored as binary data.
- `embeddings_shape`: A string representation of the shape of the embeddings.

### 6. **Testing Strategy**

- **Unit Tests**: Unit tests have been written for models, views, and API endpoints. 
- **Test Coverage**: The tests ensure that document upload, embedding storage, and query responses work as expected.
- **Test Frameworks**: The project uses `pytest`, `pytest-django`, and `pytest-cov` for testing and test coverage.

### 7. **Contributions and Improvements**

This project is open for contributions. Any improvements related to the performance of the document query mechanism or additions like document classification, more advanced NLP processing, or integration with other databases are welcome.

### 7. **Curl Command to Test the API**
-**Uploading**:curl -X POST -F "file=@Path_to_pdf\filename.pdf" http://127.0.0.1:8000/api/upload/ .
-**QuestionAnswer**curl -X POST -d "{\"question\": \"Your Question\"}" -H "Content-Type: application/json" http://127.0.0.1:8000/api/qa/ .

---

