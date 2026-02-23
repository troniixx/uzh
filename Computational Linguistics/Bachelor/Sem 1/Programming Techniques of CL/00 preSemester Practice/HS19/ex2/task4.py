print("Enter a string:")
str = input()

ger = ["heit", "keit", "chen"]
eng = ["ness", "nce", "ty"]
fr = ["que", "age"]

if str.endswith(tuple(ger)):
    print("German")
elif str.endswith(tuple(eng)):
    print("English")
elif str.endswith(tuple(fr)):
    print("French")
else:
    print("Unknown")
