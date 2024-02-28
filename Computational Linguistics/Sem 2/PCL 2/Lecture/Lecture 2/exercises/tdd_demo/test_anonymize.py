import pytest

from anonymize import anonymize_numbers, anonymize_email_address


def test_anonymize_phone_number() -> None:
    pass



# EMAIL_TESTCASES = [
#     ("info@uzh.ch", "xxxx@yyy.ch"),
#     ("simple123@example.ch", "xxxxxxxxx@yyyyyyy.ch"),
#     ("very.common@example.org", "xxxxxxxxxxx@yyyyyyy.org"),
#     ("other.email-with-hyphen@example.info", "xxxxxxxxxxxxxxxxxxxxxxx@yyyyyyy.info"),
#     ("x@example.cl.ch", "x@yyyyyyyyyy.ch"),
# ]

# @pytest.mark.parametrize("test_input,expected", EMAIL_TESTCASES)
# def test_email(test_input, expected) -> None:
#     assert anonymize_email_address(test_input) == expected

