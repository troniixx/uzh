import re


def anonymize_numbers(sms: str) -> str:
    """Find all sequences of numbers of lenght 3 or longer
    and replace each digit with an 'N'.
    """
    for c in sms:
        if c.isdigit():
            sms = sms.replace(c, 'N')
    
    return sms

def anonymize_email_address(sms: str) -> str:
    """Anonymize email addresses in input:
    replace each character in local part with X and
    replace each character in domain (except top-level) part with Y.
    Example: info@uzh.ch --> xxxx@yyy.ch
    """
    s = ""
    l, r = sms.split("@")
    
    ll, rr = r.split(".")
    
    for _ in l:
        s += "x"
        
    s += "@"
    
    for _ in ll:
        s += "y"
        
    s += "." + rr
    
    return s
    
    
if __name__ == "__main__":
    print(anonymize_numbers("I have 2 dogs and 3 cats."))
    print(anonymize_email_address("mert.erol@uzh.ch"))