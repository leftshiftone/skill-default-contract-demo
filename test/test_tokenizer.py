from src.tokenizer import NaiveTokenizer


def test_does_tokenize():
    result = NaiveTokenizer.tokenize("this is just a test")
    assert result == ["this", "is", "just", "a", "test"]