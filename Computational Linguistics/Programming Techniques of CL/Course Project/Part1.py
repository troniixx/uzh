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


# TODO: Load the spaCy model
# TODO: Load the book text


# Feel free to add more functions as needed!


# Function to process the text and perform NER
def perform_ner(text, spacy_model):
    # TODO: Process the text using the provided model and return the entities
    # Example: return nlp_model(text).ents
    pass


# Function to extract and structure entity information
def extract_entity_info(entities):
    entity_data = []
    # TODO: Iterate over entities and extract necessary information
    # Append the extracted info to entity_data
    return entity_data


# Function to save data to JSON file
def save_to_json(data, filename):
    # TODO: Save the data to a JSON file
    pass


# Main Function
def main():
    # TODO: Load your book text here
    book_text = "Your book text here."

    # Perform NER on the text
    entities = perform_ner(book_text)

    # Extract information from entities
    entity_info = extract_entity_info(entities)

    # Save the results to a JSON file
    save_to_json(entity_info, 'BookTitle_NER.json')


# Run the main function
if __name__ == "__main__":
    main()
