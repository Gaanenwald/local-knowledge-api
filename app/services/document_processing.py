from typing import Annotated

from fastapi import UploadFile, Depends

from dependencies import get_file_processing_context
from models.document import Document
from services.block_extraction import BlockExtractor
from services.document_extraction import file_validate, get_file_content


async def process_document(file: UploadFile, extension: str, extractor: BlockExtractor) -> Document:
    content = await get_file_content(file, extension)
    blocks = extractor.extract(content)

    return Document(
        filename=file.filename,
        content=content,
        extension=extension,
        size=file.size,
    )