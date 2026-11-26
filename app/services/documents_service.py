from fastapi import UploadFile

from models.document import Document
from services.block_extraction import get_block_extractor
from services.document_extraction import file_validate, get_file_content


class DocumentsService:
    async def process_document(self, file: UploadFile) -> Document:
        file_extension = file_validate(file)
        content = await get_file_content(file, file_extension)
        extractor = get_block_extractor(file_extension)
        blocks = extractor.extract(content)

        return Document(
            filename=file.filename,
            content=content,
            extension=file_extension,
            size=file.size,
        )