from fastapi import UploadFile, APIRouter

from models.document import Document
from services.document_extraction import file_validate, get_file_content

router = APIRouter()


@router.post("/documents", response_model=Document)
async def documents(file: UploadFile):
    file_extension = file_validate(file)
    content = await get_file_content(file, file_extension)

    return Document(
        filename=file.filename,
        content=content,
        extension=file_extension,
        size=file.size
    )
