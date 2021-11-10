from collections import defaultdict

# Dataset contains data that will be reverse indexed
dataset = [
    "Hello world",
    "This is the WORLD",
    "hello again"
] 

def reverse_index(dataset):

    index_dictionary = {}

    dataset2 = [d.lower().split(" ") for d in dataset]

    words = []
    for line in dataset2:
        for word in line:
            if word not in words:
                words.append(word)
    
    index_dictionary = {word: [] for word in words}

    for word in words:
        for index, line in enumerate(dataset2):
            if word in line:
                index_dictionary[word].append(index)
    
    return index_dictionary
    # don't forget to return your resulting dictionary

# You can see the output of your function here
if __name__ == '__main__':
    print(reverse_index(dataset))
