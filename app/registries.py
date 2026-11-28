from services.content_extractors import extract_markdown_text, extract_pdf_text
from services.transformers_tokenizer import TransformersTokenizer

content_extractors = {
    "md": extract_markdown_text,
    "pdf": extract_pdf_text,
}

TOKENIZER_MODELS = {
    "bge-m3": "BAAI/bge-m3",
}

TOKENIZER_BACKENDS = {
    "transformers": TransformersTokenizer,
}
