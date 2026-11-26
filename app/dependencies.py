from fastapi import UploadFile, Depends

from services.block_extraction import MarkdownBlockExtractor, PdfBlockExtractor, BlockExtractor
from services.document_extraction import file_extension_validate


def get_file_processing_context(file: UploadFile) -> tuple[str, BlockExtractor]:
    extension = file_extension_validate(file)
    extractor = block_extractors[extension]
    if not extractor:
        raise ValueError("Unsupported extension")
    return extension, extractor


block_extractors = {
    "md": MarkdownBlockExtractor(),
    "pdf": PdfBlockExtractor(),
}
