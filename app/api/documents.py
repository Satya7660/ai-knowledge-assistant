from fastapi import APIRouter, UploadFile, File

from app.services.document_service import DocumentService

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

document_service = DocumentService()


@router.post("/upload")
def upload_document(
    file: UploadFile = File(...)
):
    return document_service.upload_document(file)


@router.get("")
def list_documents():
    return document_service.list_documents()


@router.get("/{document_id}")
def get_document(document_id: int):
    return document_service.get_document(document_id)


@router.delete("/{document_id}")
def delete_document(document_id: int):
    document_service.delete_document(document_id)

    return {
        "message": "Document deleted successfully."
    }