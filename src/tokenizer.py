import itertools
from typing import List, Iterator


class NaiveTokenizer:
    """
    A very naive tokenizer for demonstration purposes
    """
    @staticmethod
    def tokenize(text: str) -> [str]:
        return text.split(" ")
