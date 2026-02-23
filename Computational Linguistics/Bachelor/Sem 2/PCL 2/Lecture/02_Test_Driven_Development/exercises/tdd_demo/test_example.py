import pytest

from example import normalize_swiss_german, foo


def test_esszett() -> None:
    test_input = "Die Vorlesung findet statt an der Andreasstraße."
    expected = "Die Vorlesung findet statt an der Andreasstrasse."
    assert normalize_swiss_german(test_input) == expected


def test_key_error() -> None:
    with pytest.raises(KeyError):
        foo(dict(b=2))


def test_esszett_upper() -> None:
    test_input = "STRAẞE"
    expected = "STRASSE"
    assert normalize_swiss_german(test_input) == expected



