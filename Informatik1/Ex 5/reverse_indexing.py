from collections import defaultdict

# Dataset contains data that will be reverse indexed
dataset = [
    "Hello world",
    "This is the WORLD",
    "hello again"] 

def reverse_index(dataset):
    
    index_dictionary = {}

    #lower casing the whole set
    lower_case_dataset = []
    for element in dataset:
        lower_case_dataset.append(element.lower())
    print(lower_case_dataset)

    #new list with each word seperated
    seperated = []
    for elements in lower_case_dataset:
        seperated.append(elements.split(' '))
    print(seperated)

    #add to dictionary
    for sublist in seperated:
        pass
            
        



    # don't forget to return your resulting dictionary
    return index_dictionary

# You can see the output of your function here
print(reverse_index(dataset))
