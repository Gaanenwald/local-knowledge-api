# from typing import Protocol
#
# from transformers import AutoTokenizer
#
# from config import settings
#
#
# class Tokenizer(Protocol):
#     def count_tokens(self, text: str) -> int:
#         ...
#
#     def encode_with_offsets(self, text: str) -> tuple[list[int], list[tuple[int, int]]]:
#         ...
#
#
# def tokenizer_init():
#     ...
