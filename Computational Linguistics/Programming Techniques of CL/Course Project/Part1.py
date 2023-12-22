"""
PCL 1 Fall Semester 2023 - Course Project
Part 0: Book Selection
Students: Mert Erol, Andrea Scheck
"""
# --- Imports ---
import os
import re
import json
import spacy
import nltk
# --- You may add other imports here ---
from tqdm import tqdm
from sys import argv

# TODO: add argv stuff
# ****** IMPORTANT: Change paths to fit your system ******
PATH_ALICE = "Computational Linguistics/Programming Techniques of CL/Course Project/Alice/Chapters"
PATH_DRACULA = "Computational Linguistics/Programming Techniques of CL/Course Project/Dracula/Chapters"
PATH_FRANKY = "Computational Linguistics/Programming Techniques of CL/Course Project/Frankenstein/Chapters"

JSON_PATH = "/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/JSON_part1"

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
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as file:
                chapters.append(file.read())
    return chapters

# function to process the text and perform NER
def perform_ner(file_path, spacy_model):
    # Open the file and read its contents
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    # Process the text with spaCy and extract entities
    ent_list = []
    doc = spacy_model(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON" and "\n" not in ent.text and ent.text in LIST_NAMES:
            ent_list.append(ent.text)

    return ent_list


# function to remove punctuation and newlines (got the regex from chatgpt)
def rem_puc(text):
    text = re.sub(r'[!"#$%&\"()*+,-./:;<=>?@[\\]^_`{|}~]', "", text) # remove punctuation
    text = re.sub(r"\n", " ", text) # replace newlines with space
    return text

# function to extract chapter number from filename (got this from chatgpt)
def extract_chapter_number(filename):
    # extract digits from filename and convert to int
    chapter_num = int(re.search(r"\d+", filename).group())
    return chapter_num

# Function to extract and structure entity information from chapters
def extract_entity_info(folder_path, spacy_model, character_list):
    # initialize data structure
    all_characters_info = {character: {"name": character, "aliases": [], "occurrences": []} for character in character_list}

    # load the chapters
    chapters = load_books_by_chapter(folder_path)
    
    # load the spaCy model
    nlp = spacy_model

    # iterate over each chapter and of course my fancy progress bar :)
    for chapter_number, chapter_text in tqdm(enumerate(chapters, start=1), total=len(chapters), desc="Processing chapters", colour = "#1E90FF"):

        # clean the chapter text
        text_clean = rem_puc(chapter_text)
        doc = nlp(text_clean)

        # iterate over the list of character names
        for ent in doc.ents:
            if ent.text in character_list:
                # Update character information
                occurrence = {
                    "sentence": ent.sent.text if ent.sent else "No sentence found",
                    "chapter": chapter_number,
                    "position": {"start": ent.start_char, "end": ent.end_char}
                }
                all_characters_info[ent.text]["occurrences"].append(occurrence)

    # convert the dictionary to the required list format
    main_characters = list(all_characters_info.values())

    return {"main_characters": main_characters}



# TODO: function to save data to JSON file using extract_entitiy_info
def save_to_json(data, file_path, file_name):
    # construct the full file path
    full_path = os.path.join(file_path, file_name + ".json")

    # save the data to a JSON file
    with open(full_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


# Main Function
def main():
    
    # DONE: Add command line arguments
    if len(argv) != 5:
        print("Usage: python3 part1.py <book_text> <book_path> <json_save_folder> <json_name>")
        print("Example: python3 part1.py Franky/franky_cleaned.txt Franky/Chapters JSON_part1 Franky_json")
    
    print("Starting NER and entity extraction... This might take a while.")
    char_list = perform_ner(argv[1], SPACY_MODEL)
    entity_info = extract_entity_info(argv[2], SPACY_MODEL, char_list)
    json_path = argv[3]
    json_name = argv[4]
    
    # DONE: Save the results to a JSON file
    save_to_json(entity_info, json_path, json_name)
    print("Done! JSON file saved to: " + json_path + "/" + json_name + ".json")


# Run the main function
if __name__ == "__main__":
    main()


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
                More occurrences
            ]
        },
        More main characters
        ]
    }

    """