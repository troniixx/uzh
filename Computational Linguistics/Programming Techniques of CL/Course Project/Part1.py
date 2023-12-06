"""
PCL 1 Fall Semester 2023 - Course Project
Part 0: Book Selection
Students: <person 1>, <person 2>
"""
# --- Imports ---
import os
import re
import json
import spacy
import nltk
# --- You may add other imports here ---

# ****** IMPORTANT: Change paths to fit your system ******
PATH_ALICE = "/Users/merterol/Desktop/VSCode/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Alice/alice_cleaned.txt"
PATH_DRACULA = "/Users/merterol/Desktop/VSCode/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Dracula/dracula_cleaned.txt"
PATH_FRANKY = "/Users/merterol/Desktop/VSCode/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Frankenstein/franky_cleaned.txt"
# ****** IMPORTANT: Change paths to fit your system ******

# DONE: Load the spaCy model
SPACY_MODEL = spacy.load("en_core_web_sm")

# set of gutenberg strings that would be considered as named entities and were not filtered by gutenberg_cleanup.py 
# these are not relevant to our analysis
# i used a set because it has faster lookup times than a normal list
GUTENBERG_BS = set(["Gutenberg", "Project Gutenberg", "Project\nGutenberg", "LIMITED WARANTY", "LIMITED WARRANTY", "Gutenberg eBooks", "Michael S. Hart"])

# DONE: Load the book text
def load_book(file_path):
    # open the file and read its contents
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    return text

# Feel free to add more functions as needed!


# Function to process the text and perform NER
def perform_ner(text, spacy_model):
    # TODO: Process the text using the provided model and return the entities
    ent_list = []
    doc = spacy_model(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON" and ent.text not in GUTENBERG_BS:
            ent_list.append(ent.text)


    return ent_list


# Function to extract and structure entity information
def extract_entity_info(entities):
    entity_data = []
    # TODO: Iterate over entities and extract necessary information
    # Append the extracted info to entity_data
    return entity_data


# Function to save data to JSON file
def save_to_json(data, filename):
    """ should look something like this:

    {
    "main_characters": [
            {
                "name": "CharacterName1",
                "aliases": ["Alias1", "Alias2"],
                "occurrences": [
                {
                    "sentence": "Context of mention.",
                    "chapter": "Chapter number",
                    "position": {"start": startIndex, "end": endIndex}
                },
                // More occurrences
            ]
        },
        // More main characters
        ]
    }

    """

    # TODO: Save the data to a JSON file
    pass


# Main Function
def main():


    # TODO: Load your book text here
    book_text = load_book(PATH_ALICE)

    # Perform NER on the text
    entities = perform_ner(book_text, SPACY_MODEL)
    print(entities)
    # Extract information from entities
    # entity_info = extract_entity_info(entities)

    # Save the results to a JSON file
    # save_to_json(entity_info, 'BookTitle_NER.json')


# Run the main function
if __name__ == "__main__":
    main()
