from fastapi import UploadFile, HTTPException
from pymupdf import pymupdf

from config import settings


def extract_markdown_text(content: bytes) -> str:
    try:
        content = content.decode("utf-8")
    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="Unicode decoding error")

    return content


def extract_pdf_text(content: bytes) -> str:
    try:
        with pymupdf.open(stream=content, filetype="pdf") as doc:
            pages_text = [page.get_text() for page in doc]
    except pymupdf.FileDataError:
        raise HTTPException(status_code=400, detail="PDF decoding error")

    return "\f".join(pages_text)


content_extractors = {
    "md": extract_markdown_text,
    "pdf": extract_pdf_text,
}


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