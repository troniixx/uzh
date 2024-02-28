import re


def normalize_swiss_german(sentence: str) -> str:
    """Replace German Esszett 'ß' with 'ss' in input sentence
    and return normalized sentence.
    """
    return re.sub("ß", "ss", sentence)


def foo(d: dict) -> None:
    """Raise a KeyError if the key 'a' is not in the input dictionary."""
    print(d["a"])
