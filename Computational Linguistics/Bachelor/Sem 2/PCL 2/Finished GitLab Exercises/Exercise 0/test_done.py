import pytest

from done import tokenize, count_most_frequent_token

def test_tokenize():
    assert tokenize("I commenced by inuring my body to hardship.") == ["I", "commenced", "by", "inuring", "my", "body", "to", "hardship", "."]

def test_count_most_frequent_token():
    tokens = [
        "I", "have", "read", "with", "ardour", "the", "accounts", "of", "the", 
        "various", "voyages", "which", "have", "been", "made", "in", "the", 
        "prospect", "of", "arriving", "at", "the", "North", "Pacific", "Ocean", 
        "through", "the", "seas", "which", "surround", "the", "pole", "."
        ]
    assert count_most_frequent_token(tokens) == "the"
