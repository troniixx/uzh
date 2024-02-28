import re


def anonymize_numbers(sms: str) -> str:
    """Find all sequences of numbers of lenght 3 or longer
    and replace each digit with an 'N'.
    """
    for c in sms:
        if c.isdigit():
            sms = sms.replace(c, 'N')
    
    return sms

def anonymize_email_address(email: str) -> str:
    """Anonymize email addresses in input:
    replace each character in local part with X and
    replace each character in domain (except top-level) part with Y.
    Example: info@uzh.ch --> xxxx@yyy.ch
    """
    # Split the email address into the local part and the domain part
    local_part, domain_part = email.split('@')
    # Further split the domain part into the domain and the top-level domain
    domain, top_level_domain = domain_part.rsplit('.', 1)
    # Replace all characters in the local part with 'x'
    anonymized_local = 'x' * len(local_part)
    # Replace all characters in the domain with 'y'
    anonymized_domain = 'y' * len(domain)
    # Combine everything back together
    return f"{anonymized_local}@{anonymized_domain}.{top_level_domain}"
    
    
if __name__ == "__main__":
    print(anonymize_numbers("I have 2 dogs and 3 cats."))
    print(anonymize_email_address("mert.erol@uzh.ch"))