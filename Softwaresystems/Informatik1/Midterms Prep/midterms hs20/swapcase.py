def swapcase(string):
    sol = ""

    if string == "":
        raise ValueError("Du huresohn")

    for char in string:
        if char.isupper():
            sol += char.lower()
        if char.islower():
            sol += char.upper()
        if not char.isalpha():
            sol += char

    return sol

if __name__ == '__main__':
    print(swapcase("HeLlO"))
    print(swapcase("Hallo!"))
    print(swapcase(""))