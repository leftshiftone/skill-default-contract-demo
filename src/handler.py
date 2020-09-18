import logging

from src.tokenizer import NaiveTokenizer

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("skill")


def evaluate(payload: dict, context: dict) -> dict:
    text = payload["text"]
    return {'tokens': NaiveTokenizer.tokenize(text)}


def on_started(context):
    log.info("on_started triggered")
