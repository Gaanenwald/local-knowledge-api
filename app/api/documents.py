from fastapi import UploadFile

from main import app, file_validate, get_file_content
from models.document import Document


@app.post("/documents", response_model=Document)
async def documents(file: UploadFile):
    file_extension = file_validate(file)
    content = await get_file_content(file, file_extension)

    return Document(
        filename=file.filename,
        content=content,
        extension=file_extension,
        size=file.size
    )