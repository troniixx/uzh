##############################################################################################################
##############################################################################################################
##### DO NOT MODIFY THIS CODE #####
# This code is to be used as is.
# author: Mert Erol, Andrea Eva Scheck

import os
import sys
import re
from tqdm import tqdm

# Markers for the start and end of Project Gutenberg headers/footers
TEXT_START_MARKERS = frozenset((
    "*END*THE SMALL PRINT",
    "*** START OF THE PROJECT GUTENBERG",
    "*** START OF THIS PROJECT GUTENBERG",
    "This etext was prepared by",
    "E-text prepared by",
    "Produced by",
    "Distributed Proofreading Team",
    "Proofreading Team at http://www.pgdp.net",
    "http://gallica.bnf.fr)",
    "      http://archive.org/details/",
    "http://www.pgdp.net",
    "by The Internet Archive)",
    "by The Internet Archive/Canadian Libraries",
    "by The Internet Archive/American Libraries",
    "public domain material from the Internet Archive",
    "Internet Archive)",
    "Internet Archive/Canadian Libraries",
    "Internet Archive/American Libraries",
    "material from the Google Print project",
    "*END THE SMALL PRINT",
    "***START OF THE PROJECT GUTENBERG",
    "This etext was produced by",
    "*** START OF THE COPYRIGHTED",
    "The Project Gutenberg",
    "http://gutenberg.spiegel.de/ erreichbar.",
    "Project Runeberg publishes",
    "Beginning of this Project Gutenberg",
    "Project Gutenberg Online Distributed",
    "Gutenberg Online Distributed",
    "the Project Gutenberg Online Distributed",
    "Project Gutenberg TEI",
    "This eBook was prepared by",
    "http://gutenberg2000.de erreichbar.",
    "This Etext was prepared by",
    "This Project Gutenberg Etext was prepared by",
    "Gutenberg Distributed Proofreaders",
    "Project Gutenberg Distributed Proofreaders",
    "the Project Gutenberg Online Distributed Proofreading Team",
    "**The Project Gutenberg",
    "*SMALL PRINT!",
    "More information about this book is at the top of this file.",
    "tells you about restrictions in how the file may be used.",
    "l'authorization à les utilizer pour preparer ce texte.",
    "of the etext through OCR.",
    "*****These eBooks Were Prepared By Thousands of Volunteers!*****",
    "We need your donations more than ever!",
    " *** START OF THIS PROJECT GUTENBERG",
    "****     SMALL PRINT!",
    '["Small Print" V.',
    '      (http://www.ibiblio.org/gutenberg/',
    'and the Project Gutenberg Online Distributed Proofreading Team',
    'Mary Meehan, and the Project Gutenberg Online Distributed Proofreading',
    '                this Project Gutenberg edition.',
))


TEXT_END_MARKERS = frozenset((
    "*** END OF THE PROJECT GUTENBERG",
    "*** END OF THIS PROJECT GUTENBERG",
    "***END OF THE PROJECT GUTENBERG",
    "End of the Project Gutenberg",
    "End of The Project Gutenberg",
    "Ende dieses Project Gutenberg",
    "by Project Gutenberg",
    "End of Project Gutenberg",
    "End of this Project Gutenberg",
    "Ende dieses Projekt Gutenberg",
    "        ***END OF THE PROJECT GUTENBERG",
    "*** END OF THE COPYRIGHTED",
    "End of this is COPYRIGHTED",
    "Ende dieses Etextes ",
    "Ende dieses Project Gutenber",
    "Ende diese Project Gutenberg",
    "**This is a COPYRIGHTED Project Gutenberg Etext, Details Above**",
    "Fin de Project Gutenberg",
    "The Project Gutenberg Etext of ",
    "Ce document fut presente en lecture",
    "Ce document fut présenté en lecture",
    "More information about this book is at the top of this file.",
    "We need your donations more than ever!",
    "END OF PROJECT GUTENBERG",
    " End of the Project Gutenberg",
    " *** END OF THIS PROJECT GUTENBERG",
))


LEGALESE_START_MARKERS = frozenset(("<<THIS ELECTRONIC VERSION OF",))


LEGALESE_END_MARKERS = frozenset(("SERVICE THAT CHARGES FOR DOWNLOAD",))

def strip_headers(text):
    """Remove lines that are part of the Project Gutenberg header or footer."""
    lines = text.splitlines()
    sep = str(os.linesep)

    out = []
    i = 0
    footer_found = False
    ignore_section = False

    for line in lines:
        reset = False

        # Header removal
        if i <= 600 and any(line.startswith(token) for token in TEXT_START_MARKERS):
            reset = True

        if reset:
            out = []
            continue

        # Footer detection
        if i >= 100 and any(line.startswith(token) for token in TEXT_END_MARKERS):
            footer_found = True

        if footer_found:
            break

        # Legalese removal
        if any(line.startswith(token) for token in LEGALESE_START_MARKERS):
            ignore_section = True
            continue
        elif any(line.startswith(token) for token in LEGALESE_END_MARKERS):
            ignore_section = False
            continue

        if not ignore_section:
            out.append(line.rstrip(sep))
            i += 1

    return sep.join(out)

##############################################################################################################
##############################################################################################################

#### MODIFY HERE ####

#DONE: Implement the function split_book_by_chapter

def split_book_by_chapter(cleaned_text, book_title):
    """
    Implement a function that splits the book into chapters and saves 
    each chapter in a separate file in a folder named after the book title.
    """
    # Add your code here to split the cleaned_text into chapters and save each chapter in a separate file
    pattern = r'\b(?:CHAPTER|Chapter|Letter)\s+(?:[A-Z0-9]+|[0-9]+)\.?\n+' # Regex pattern to split the text into chapters
    chapters = re.split(pattern, cleaned_text)[1:]
    length = len(chapters) # Get the length of the chapters list (used in my fancy progess bar :D)
    
    # create a new txt file with the corresponding chapter number and 
    # save the chapter in it while ingoring the empty chapters &
    # "chapters" with just the title in it
    chapter_number = 0
    for chapter in chapters:
        # Check if the chapter is not just whitespace
        if chapter.strip():
            chapter_number += 1  # Increment chapter number only for non-empty chapters
            filename = os.path.join(book_title, "Chapters", f"chapter_{chapter_number}.txt")
            with open(filename, "w") as file:
                file.write(chapter.strip())
    
    # Always wanted to have a progess bar in my code, so here it is! :)
    for _ in tqdm(range(length), total = length, colour = "#1E90FF", desc = "Splitting into chapters..."):
        pass
    
    print("Splitting into chapters Successful!")


#DONE: Implement the main function
def main():
    """
    Processes a Gutenberg book text file for cleanup and chapter-wise separation.

    Reads and cleans a book text file specified by the command line argument. Saves 
    the cleaned text in a book-named directory, and splits it into chapters saved 
    in a 'chapters' subfolder within this directory.

    Expects two command line arguments:
    1. Path to the original book file.
    2. Path to the output base directory.

    Creates output directories and files, and prints relevant success messages and paths.
    
    Example usage:
        python3 gutenberg_cleanup.py alice.txt Alice_in_Wonderland
    """
    
    # Did a small change here to make sure the user enters the correct number of arguments with my usage version
    # --> User specifies the name of the new directory that gets created to store the data
    if len(sys.argv) != 3:
        print("Invalid number of arguments! Make sure to be in the correct directory where all files and/or folders are located.")
        print("Usage: python gutenberg_cleanup.py <path_to_book_file> <new_name_of_the_book_folder>")
        sys.exit(1)

    file_path = sys.argv[1] # Gutenberg Book Path
    dir_book = sys.argv[2] # Path of "Title" Folder
    book_title = os.path.basename(file_path).replace('.txt', '') #get book title from path
    dir_clean = os.path.join(dir_book, book_title + "_cleaned.txt") # directory where the cleaned text will be saved

    os.makedirs(dir_book) # create a folder named after the book title
    os.makedirs(os.path.join(dir_book, "Chapters")) # create a folder named 'Chapters' inside the book title folder
    
    # read the text file
    with open(file_path, "r", encoding = "utf-8") as file:
        text = file.read()
        # clean the text
        cleaned_text = strip_headers(text)
        # save the cleaned text in the book title folder
        with open(dir_clean, "w") as dir:
            dir.write(cleaned_text)
    
    # Always wanted to have a progess bar in my code, so here it is! :)
    for _ in tqdm(range(len(cleaned_text)), colour = "#1E90FF", desc = "Cleaning up..."):
        pass
    
    print("Cleanup Successful!")
    print("Cleaned text saved in: " + dir_clean + "\n")

    split_book_by_chapter(cleaned_text, dir_book)

# standard main function
if __name__ == '__main__':
    main()