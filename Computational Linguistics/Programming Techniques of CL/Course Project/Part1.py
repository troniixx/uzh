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
from sys import argv

# TODO: add argv stuff
# ****** IMPORTANT: Change paths to fit your system ******
PATH_ALICE = "Computational Linguistics/Programming Techniques of CL/Course Project/Alice/Chapters"
PATH_DRACULA = "Computational Linguistics/Programming Techniques of CL/Course Project/Dracula/Chapters"
PATH_FRANKY = "Computational Linguistics/Programming Techniques of CL/Course Project/Frankenstein/Chapters"

PATH_ALICE_NMSG = "/Users/merterol/Desktop/VSCode/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Alice/Chapters"
PATH_DRACULA_NMSG = "/Users/merterol/Desktop/VSCode/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Dracula/Chapters"
PATH_FRANKY_NMSG = "/Users/merterol/Desktop/VSCode/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Franky/Chapters"
# ****** IMPORTANT: Change paths to fit your system ******

# DONE: Load the spaCy model
SPACY_MODEL = spacy.load("en_core_web_sm")

# set of names we used for main character analysis
# i used a set because it has faster lookup times than a normal list
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

# function to process the text and perform NER
def perform_ner(text, spacy_model):
    # DONE: Process the text using the provided model and return the entities

    ent_list = []
    doc = spacy_model(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON" and "\n" not in ent.text and ent.text in LIST_NAMES:
            ent_list.append(ent.text)

    return ent_list

# function to remove punctuation and newlines (got the regex from chatgpt)
def rem_puc(text):
    text = re.sub(r'[!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]', '', text) # remove punctuation
    text = re.sub(r'\n', ' ', text) # replace newlines with space
    return text

# function to extract chapter number from filename (got this from chatgpt)
def extract_chapter_number(filename):
    # extract digits from filename and convert to int
    chapter_num = int(re.search(r'\d+', filename).group())
    return chapter_num

# Function to extract and structure entity information from chapters
def extract_entity_info(folder_path, spacy_model, character_list):
    # initialize data structure
    all_chapters_info = {"main_characters": []}

    # load the spaCy model
    nlp = spacy_model

    # iterate over sorted chapter files
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith('.txt'):
            chapter_path = os.path.join(folder_path, filename)
            with open(chapter_path, 'r', encoding='utf-8') as file:
                chapter_text = file.read()

            # clean the chapter text
            text_clean = rem_puc(chapter_text)
            doc = nlp(text_clean)

            # extract chapter number from filename
            chapter_number = extract_chapter_number(filename)

            # iterate over the list of character names
            for character in character_list:
                character_info = {
                    "name": character,
                    "aliases": [],  # TODO: add aliases here
                    "occurrences": []
                }

                # iterate over the entities in the document
                for ent in doc.ents:
                    if ent.text == character:
                        start_idx = ent.start_char
                        end_idx = ent.end_char
                        sentence = ent.sent.text if ent.sent else "No sentence found"

                        occurrence = {
                            "sentence": sentence,
                            "chapter": chapter_number,
                            "position": {"start": start_idx, "end": end_idx}
                        }

                        character_info["occurrences"].append(occurrence)

                if character_info["occurrences"]:
                    all_chapters_info["main_characters"].append(character_info)

    return all_chapters_info


# TODO: function to save data to JSON file
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

    # Perform NER on the text
    #print("Entities")
    #entities = perform_ner(book_text, SPACY_MODEL)
    #print(entities)
    # Extract information from entities
    print("Entity info:")
    entity_info = extract_entity_info(PATH_ALICE_NMSG, SPACY_MODEL, LIST_NAMES)
    print(entity_info)
    
    # Save the results to a JSON file
    # save_to_json(entity_info, "BookTitle_NER.json")


# Run the main function
if __name__ == "__main__":
    main()
