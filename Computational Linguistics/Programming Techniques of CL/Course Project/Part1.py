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
import tqdm

# ****** IMPORTANT: Change paths to fit your system ******
PATH_ALICE = "Computational Linguistics/Programming Techniques of CL/Course Project/Alice/alice_cleaned.txt"
PATH_DRACULA = "Computational Linguistics/Programming Techniques of CL/Course Project/Dracula/dracula_cleaned.txt"
PATH_FRANKY = "Computational Linguistics/Programming Techniques of CL/Course Project/Frankenstein/franky_cleaned.txt"

PATH_ALICE_NMSG = "/Users/merterol/Desktop/VSCode/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Alice/alice_cleaned.txt"
PATH_DRACULA_NMSG = "/Users/merterol/Desktop/VSCode/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Dracula/dracula_cleaned.txt"
PATH_FRANKY_NMSG = "/Users/merterol/Desktop/VSCode/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Franky/franky_cleaned.txt"
# ****** IMPORTANT: Change paths to fit your system ******

# DONE: Load the spaCy model
SPACY_MODEL = spacy.load("en_core_web_sm")

# set of gutenberg strings that would be considered as named entities and were not filtered by gutenberg_cleanup.py 
# these are not relevant to our analysis
# i used a set because it has faster lookup times than a normal list
GUTENBERG_BS = set(["Gutenberg", "Project Gutenberg", "Project\nGutenberg", "LIMITED WARANTY", "LIMITED WARRANTY", "Gutenberg eBooks", "Michael S. Hart"])
LIST_NAMES = set(["Alice", "Queen", "King", "Gryphon", "Hatter", "Mock Turtle", "Duchess", "Dormouse", "Mouse", "Rabbit", "Elizabeth", "Clerval",
            "Justine", "Felix", "Victor", "Safie", "Henry", "William", "Agatha", "Kirwin", "Van Helsing", 
            "Lucy", "Jonathan", "Count", "Arthur","Seward", "Mina", "Quincey", "Renfield"])

# DONE: Load the book text
def load_books_by_chapter(folder_path):
    chapters = []
    # Sorting files to ensure they are in order
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith('.txt'):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                chapters.append(file.read())
    return chapters

# Feel free to add more functions as needed!
def rem_puc(text):
    text = re.sub(r"[^\w\s]")
    text = re.sub(r'\n', ' ', text)  # Replace newlines with space
    return text



# Function to process the text and perform NER
def perform_ner(text, spacy_model):
    # TODO: Process the text using the provided model and return the entities

    ent_list = []
    doc = spacy_model(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON" and ent.text not in GUTENBERG_BS and "\n" not in ent.text:
            ent_list.append(ent.text)

    return ent_list

def get_chapter_number(sentence):
    

# TODO: Function to extract and structure entity information
def extract_entity_info(text):
    # Clean the text
    text_clean = rem_puc(text)
    doc = SPACY_MODEL(text_clean)

    # Initialize data structure
    main_characters = []

    # Iterate over the list of character names
    for character in LIST_NAMES:
        character_info = {
            "name": character,
            "aliases": [],  # Add aliases if you have them
            "occurrences": []
        }

        # Iterate over the entities in the document
        for ent in doc.ents:
            if ent.text == character:
                start_idx = ent.start_char
                end_idx = ent.end_char
                sentence = ent.sent.text if ent.sent else "No sentence found"
                chapter_number = get_chapter_number(ent.sent)  # TODO implement this function

                occurrence = {
                    "sentence": sentence,
                    "chapter": chapter_number,
                    "position": {"start": start_idx, "end": end_idx}
                }

                character_info["occurrences"].append(occurrence)

        if character_info["occurrences"]:
            main_characters.append(character_info)

    return {"main_characters": main_characters}




# TODO: Function to save data to JSON file
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
    #print("Entities")
    #entities = perform_ner(book_text, SPACY_MODEL)
    #print(entities)
    # Extract information from entities
    print("Entity info:")
    entity_info = extract_entity_info(book_text)
    print(entity_info)
    
    # Save the results to a JSON file
    # save_to_json(entity_info, "BookTitle_NER.json")


# Run the main function
if __name__ == "__main__":
    main()
