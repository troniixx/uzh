def count_keywords(path, keywords):
    words = []
    sol = dict()    

    with open(path) as file:
        for line in file:
            for word in line.split():
                words.append(word.lower())

        for element in words:
            if element in keywords:
                if element in sol:
                    sol[element] += 1
                else: sol[element] = 1
            else:
                continue

    return sol


print(count_keywords("/Users/merterol/Desktop/uzhpython/uzh/Informatik1/MidtermsInfk/midterms hs19/text.txt", ["forest", "the", "found"]))
print(count_keywords("/Users/merterol/Desktop/uzhpython/uzh/Informatik1/MidtermsInfk/midterms hs19/text.txt", ["black"]))
print(count_keywords("/Users/merterol/Desktop/uzhpython/uzh/Informatik1/MidtermsInfk/midterms hs19/text.txt", []))