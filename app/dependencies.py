from fastapi import UploadFile

from services.block_extraction import MarkdownBlockExtractor, PdfBlockExtractor, BlockExtractor
from services.document_extraction import file_extension_validate


def get_block_extractor(file_extension: str) -> BlockExtractor:
    extractor = block_extractors[file_extension]
    if not extractor:
        raise ValueError("Unsupported extension")
    return extractor


block_extractors = {
    "md": MarkdownBlockExtractor(),
    "pdf": PdfBlockExtractor(),
}
