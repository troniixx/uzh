def shout(text):
    exclams = text.count("!")
    if exclams == 0: exclams = 1
    return text.upper() + exclams * "!"

print(shout("Hello, God"))
print(shout("Hello, World!"))
print(shout("Hello! World?"))

#assert(shout("Hello, God") == "HELLO, GOD!")
#assert(shout("Hello, World!") == "HELLO, WORLD!!")
#assert(shout("Hello! World?") == "HELLO! WORLD?!")