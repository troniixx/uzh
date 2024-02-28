import re


def normalize_swiss_german(sentence: str) -> str:
    """Replace German Esszett 'ß' with 'ss' in input sentence
    and return normalized sentence.
    """
    if sentence.isupper():
        normalized_sentence = re.sub("[ßẞ]", "SS", sentence)
    else:
        normalized_sentence = re.sub("[ßẞ]", "ss", sentence)
    return normalized_sentence


def foo(d: dict) -> None:
    """Raise a KeyError if the key 'a' is not in the input dictionary."""
    print(d["a"])
