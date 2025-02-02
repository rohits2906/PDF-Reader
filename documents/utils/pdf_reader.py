import PyPDF2

class PDFReader:
    @staticmethod
    def extract_text(file):
        """
        Extract text from a PDF file using PyPDF2.
        This method works with InMemoryUploadedFile from Django.
        """
        # Read the in-memory file (file is an InMemoryUploadedFile object)
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
        return text
