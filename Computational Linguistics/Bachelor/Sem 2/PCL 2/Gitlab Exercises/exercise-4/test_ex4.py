import pytest

from ex4 import repeat_string, remove_long_tokens, filter_punctuation, lowercase, length_sort, alphabetical_sort, uppercase, Alphabet


@pytest.mark.parametrize("repeat_count, text, expected_output", [
    (5, "test", "testtesttesttesttest"),
    (3, "hello", "hellohellohello"),
    (0, "abc", ""),
    (2, "", ""),
])
def test_repeat_string(repeat_count, text, expected_output):
    repeated_text = repeat_string(text, repeat_count)
    assert repeated_text == expected_output


def test_remove_long_tokens():
    tokens = ["I", "am", "excited", "!"]
    max_length = 5
    expected_output = ["I", "am", "!"]
    output = remove_long_tokens(tokens, max_length)
    # Check that the function returns the expected output
    assert output == expected_output
    # Check that the function does not modify the input
    assert tokens != output, "The function should return a new list and not modify the input list"


@pytest.mark.parametrize("tokens, expected_output", [
    (["I", "love", "punctuation", ".", "But", "why", "?"], ["I", "love", "punctuation", "But", "why"]),
    ([], []),
    ([".", ",", "!", "?", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", "-", "/", ":", ";", "<", "=", ">", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"], []),
])
def test_filter_punctuation(tokens, expected_output):
    assert filter_punctuation(tokens) == expected_output


@pytest.mark.parametrize("tokens, expected_output", [
        (["I", "LOVE", "CAPS"], ["i", "love", "caps"]),
        (["I", "love", "CAPS"], ["i", "love", "caps"]),
        (["i", "love", "caps"], ["i", "love", "caps"]),
        ([""], [""]),
        (["123", "456", "789"], ["123", "456", "789"]),
        (["!@#", "$%^", "&*("], ["!@#", "$%^", "&*("]),
        (["AbC", "dEf", "gHi"], ["abc", "def", "ghi"]),
    ])
def test_lowercase(tokens, expected_output):
    assert lowercase(tokens) == expected_output


@pytest.mark.parametrize("tokens, expected_output", [
    (["Today", "is", "a", "great", "day"], ["Today", "great", "day", "is", "a"]),
    ([], []),
    (["day"], ["day"]),
    (["a", "bb", "ccc", "dddd"], ["dddd", "ccc", "bb", "a"]),
])
def test_length_sort(tokens, expected_output):
    assert length_sort(tokens) == expected_output


@pytest.mark.parametrize("tokens, expected_output", [
    (["apple", "banana", "cherry"], ["APPLE", "BANANA", "CHERRY"]),
    (["cherry", "banana", "apple"], ["APPLE", "BANANA", "CHERRY"]),
    (["banana", "cherry", "apple"], ["APPLE", "BANANA", "CHERRY"]),
    (["cherry", "apple", "banana"], ["APPLE", "BANANA", "CHERRY"]),
    ([], []),
    (["apple"], ["APPLE"]),
    (["1apple", "3banana", "2cherry"], ["1APPLE", "2CHERRY", "3BANANA",]),
    (["a", "bb", "ccc"], ["A", "BB", "CCC"]),
])
def test_alphabetical_sort_uppercase(tokens, expected_output):
    assert alphabetical_sort(tokens) == expected_output

    
@pytest.mark.parametrize("input, expected_output", [
    (["hello", "world"], ["HELLO", "WORLD"]),
    ([], []),
    (["hello"], ["HELLO"]),
    (["@hello", "123world"], ["@HELLO", "123WORLD"]),
    (["a", "bb", "ccc", "dddd"], ["A", "BB", "CCC", "DDDD"]),
])
def test_uppercase_decorator(input, expected_output):
    @uppercase
    def dummy_function():
        return input
    assert dummy_function() == expected_output


def test_alphabet_generator():
    alphabet = Alphabet("vffgbxyhcdqrptwocjippfeczwtnpcm")
    
    for expected, output in zip("bcdefghijmnopqrtvwxyz", alphabet):
        assert expected == output