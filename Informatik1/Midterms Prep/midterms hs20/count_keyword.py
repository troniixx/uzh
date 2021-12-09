# count_keyword_occurrence("This is a short sentence which serves as an example.",["is", "short"])
# should return 3 because "is" occurs twice and "short" occurs once.

def count_keyword_occurrence(string, strings_to_be_searched):
    counter = 0
    split = []
    split.append(string.split(" "))

    for word in split[0]:
        if word in strings_to_be_searched:
            counter += 1
        else: continue
    
    print(split)

    return counter

if __name__ == '__main__':
    print(count_keyword_occurrence("This is a short sentence which serves as an example. He is a short man who likes to play short.", ["is", "short"]))

