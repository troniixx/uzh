def validate_username(username):
    special = ["_", "."]

    if len(username) < 3:
        return tuple((False, "Username is too short!"))

    if len(username) > 16:
        return tuple((False, "Username is too long!"))
    
    if not username[0].isupper():
        return tuple((False, "Username does not start with an uppercase letter!"))

    for char in username:
        if not char.isalpha() and not char in special:
            return tuple((False, "Username contains invalid character!"))
        else: return tuple((True, None))


print(validate_username("aa"))
print(validate_username("Valid_username"))