from pathlib import Path
import shutil

from fastapi import UploadFile

from app.repositories.document_repository import DocumentRepository
from app.documents.parser import DocumentParser


class DocumentService:

    def __init__(self):
        self.repository = DocumentRepository()
        self.parser = DocumentParser()
        
        self.upload_directory = Path("uploads")
        self.upload_directory.mkdir(exist_ok=True)
        
    def upload_document(self, file: UploadFile):

        file_path = self.upload_directory / file.filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        document_id = self.repository.create_document(
            filename=file.filename,
            filepath=str(file_path)
        )

        document_text = self.parser.parse(str(file_path))
        return {
            "message": "Document uploaded successfully.",
            "id": document_id,
            "filename": file.filename,
            "filepath": str(file_path),
            "text": document_text
        }

    def get_document(self, document_id):
        return self.repository.get_document(document_id)

    def list_documents(self):
        return self.repository.list_documents()

    def delete_document(self, document_id):
        return self.repository.delete_document(document_id)

