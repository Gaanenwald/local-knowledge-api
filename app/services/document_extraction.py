from fastapi import UploadFile, HTTPException
from pymupdf import pymupdf

from config import settings
from registries import content_extractors





def file_validate(file: UploadFile):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file name provided")

    if file.size > settings.max_upload_size:
        raise HTTPException(status_code=413, detail="File too large")

    return file_extension_validate(file)


def file_extension_validate(file: UploadFile) -> str:
    rsplit_res = file.filename.rsplit('.', 1)

    if len(rsplit_res) < 2:
        raise HTTPException(status_code=400, detail="No file part")

    if rsplit_res[-1].lower() not in settings.app_extensions:
        raise HTTPException(status_code=415, detail="Unsupported file type")

    return rsplit_res[-1].lower()


async def get_file_content(file: UploadFile, extension: str) -> str:
    content = await file.read()
    return content_extractors[extension](content)
