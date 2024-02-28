import pytest

from anonymize import anonymize_numbers, anonymize_email_address

PHONE_TESTCASES = [("I have 2 dogs and 3 cats.", "I have N dogs and N cats."),
                    ("0812348991", "NNNNNNNNNN"), ("+41 44 634 22 11", "+NN NNN NNN NN NN"),
                    ("+41 44 634 22 11", "+NN NNN NNN NN NN")
                ]
@pytest.mark.parametrize("test_input,expected", PHONE_TESTCASES)
def test_anonymize_phone_number(test_input, expected) -> None:
    assert anonymize_email_address(test_input) == expected



EMAIL_TESTCASES = [
    ("info@uzh.ch", "xxxx@yyy.ch"),
    ("simple123@example.ch", "xxxxxxxxx@yyyyyyy.ch"),
    ("very.common@example.org", "xxxxxxxxxxx@yyyyyyy.org"),
    ("other.email-with-hyphen@example.info", "xxxxxxxxxxxxxxxxxxxxxxx@yyyyyyy.info"),
    ("x@example.cl.ch", "x@yyyyyyyyyy.ch"),
]

@pytest.mark.parametrize("test_input,expected", EMAIL_TESTCASES)
def test_email(test_input, expected) -> None:
    assert anonymize_email_address(test_input) == expected

