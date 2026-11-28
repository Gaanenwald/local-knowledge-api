from transformers import AutoTokenizer


class TransformersTokenizer:
    def __init__(self, model_name: str):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)

    def encode(self, text: str) -> list[int]:
        return self.tokenizer.encode(text, add_special_tokens=False)

    def count_tokens(self, text: str) -> int:
        return len(self.encode(text))

    def encode_with_offsets(self, text: str) -> tuple[list[int], list[tuple[int, int]]]:
        ...
