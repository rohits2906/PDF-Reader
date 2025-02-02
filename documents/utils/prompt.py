class Prompt:
    @staticmethod
    def create_prompt(question, document):
        return f"Question: {question}\nContext: {document.content}"
