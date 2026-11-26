from fastapi import UploadFile, APIRouter, Depends

from dependencies import get_file_processing_context
from models.document import Document
from services.block_extraction import BlockExtractor
from services.document_processing import process_document

router = APIRouter()


@router.post("/documents", response_model=Document)
async def documents(file: UploadFile, deps: tuple[str, BlockExtractor] = Depends(get_file_processing_context)):
    return await process_document(file, *deps)
