import pytest

from anonymize import anonymize_numbers, anonymize_email_address

PHONE_TESTCASES = [
                    ("081 234 89 91", "NNN NNN 89 91"), ("+41 44 634 22 11", "+41 44 NNN 22 11"),
                    ("+41 44 634 22 11", "+41 44 NNN 22 11"), ("My number is 1234567890", "My number is NNNNNNNNNN"),
                    ("Call me at 555-1234", "Call me at NNN-NNNN"),
                    ("Emergency number: 112", "Emergency number: NNN"),
                    ("Fax: 123-456-789", "Fax: NNN-NNN-NNN"),
                    ("Dial +1 (800) 123-4567 for support", "Dial +1 (NNN) NNN-NNNN for support"),
                    ("My extension is 987", "My extension is NNN"),
                    ("Contact: +49 30 12345678", "Contact: +49 30 NNNNNNNN")
                ]

@pytest.mark.parametrize("test_input,expected", PHONE_TESTCASES)
def test_anonymize_phone_number(test_input, expected) -> None:
    assert anonymize_numbers(test_input) == expected



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

