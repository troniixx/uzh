def shout(text):
    sol = ""
    for char in text:
        sol += char.upper()

    if "!" not in text:
        sol += "!"
    else:
        x = text.find("!")
        sol += sol[x]
    
    return sol

print(shout("Hello, God"))
print(shout("Hello, World!"))
print(shout("Hello! World?"))

#assert(shout("Hello, God") == "HELLO, GOD!")
#assert(shout("Hello, World!") == "HELLO, WORLD!!")
#assert(shout("Hello! World?") == "HELLO! WORLD?!")