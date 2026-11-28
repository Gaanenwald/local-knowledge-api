from fastapi import HTTPException
from pymupdf import pymupdf


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