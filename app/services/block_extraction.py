from typing import Protocol

from services.markdown_parser import extract_markdown_blocks


class BlockExtractor(Protocol):
    def extract(self, content: str) -> list[dict]:
        ...


class MarkdownBlockExtractor:
    def extract(self, content: str) -> list[dict]:
        return extract_markdown_blocks(content)


class PdfBlockExtractor:
    def extract(self, content: str) -> list[dict]:
        # TODO: implement PDF structural extraction
        return []


def get_block_extractor(file_extension: str) -> BlockExtractor:
    extractor = block_extractors.get(file_extension)
    if not extractor:
        raise ValueError("Unsupported extension")
    return extractor


block_extractors = {
    "md": MarkdownBlockExtractor(),
    "pdf": PdfBlockExtractor(),
}
