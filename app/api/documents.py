from fastapi import UploadFile, APIRouter, Depends

from models.document import Document
from services.documents_service import DocumentsService

router = APIRouter()


@router.post("/documents", response_model=Document)
async def documents(file: UploadFile, service: DocumentsService = Depends()):
    return await service.process_document(file)
