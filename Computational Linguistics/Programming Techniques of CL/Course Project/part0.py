"""
PCL 1 Fall Semester 2023 - Course Project
Part 0: Book Selection
Students: Mert Erol, Andrea Eva Scheck
"""

# --- Imports ---
import os
import re
import json
# --- Don't add other imports here ---

def json_conversion(data):
    """
    Create a function to convert the data to a json string here
    """
    
    return json.dumps(data, indent = 4)


def write_as_json(data, file_path):
    """
    Create a function to write your json string to a file here.
    Think about a naming convention for the output files.
    """
    
    with open(file_path, "w") as file:
        file.write(json_conversion(data))

# With every hour of my sanity fading i somehow managed to create this thing
# It works somehow so please so i guess i'm happy :D
def extractor_named(file_path):
    """
    Create a function to extract the named entities and sentiment expressions from the text here.
    The function should help return a json file with the following structure:
    {
        "Named Entities": [
            [int, str], ....
            ]
            """
            
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
        parts = text.split("Sentiment Expressions:")

        # splitting the text into two parts, one for the named entities and one for the sentiment expressions
        named_entities = parts[0].split("Named Entities:")[1].strip()
        """
        parts[0]: splits the named entities from the sentiment expressions
        .split("Named Entities:"): splits the parts using "named entities" as the delimiter
            e.g. "Named Entities: 12 Rabbit" -> ["", "12 Rabbit"]
            
        [1]: selects the second part of the split
            e.g. ["", "12 Rabbit"] -> "12 Rabbit"
            
        .strip(): removes the whitespace from the beginning and end of the string
            e.g. " 12 Rabbit " -> "12 Rabbit"
        """
        
        # creating two empty lists for the named entities and sentiment expressions
        named_list = []

        # process each line in the Named Entities section we split out before
        for entity_line in named_entities.split("\n"):
            entity_line = entity_line.strip()
            if entity_line:
                comp = entity_line.split(" ", 1) #splitting e.g "12 Rabbit" into "12" and "Rabbit"
                if len(comp) == 2 and comp[0].isdigit(): #checking if the first part is a number and if there is one
                    named_list.append((int(comp[0]), comp[1].strip())) # adding the tuple to the list as (int, str)

        return {
            "Named Entities": named_list,
        }

def extractor_sentiment(file_path):
        """
        Create a function to extract the named entities and sentiment expressions from the text here.
        The function should help return a json file with the following structure:
        {
        "Sentiment Expressions": [
            [int, str], ....
            ]
        }
        """

        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
            parts = text.split("Sentiment Expressions:")

            # removes whitespaces from the second part of our split
            sentiment_expressions = parts[1].strip()
            sentiment_list = []
            # process each line in the Sentiment Expressions section we split out before
            for expression_line in sentiment_expressions.split("\n"):
                expression_line = expression_line.strip()
                if expression_line:
                    comp = expression_line.split(" ", 1) #splitting e.g "12 Rabbit" into "12" and "Rabbit"
                    if len(comp) == 2 and comp[0].isdigit(): #checking if the first part is a number and if there is one
                        sentiment_list.append((int(comp[0]), comp[1].strip())) # adding the tuple to the list as (int, str)
                    
                    
        return {"Sentiment Expressions": sentiment_list}

def json_sent(txt_files_sent, output_dir_sent):
    # checks if the output directory exists, if not it creates it
    if not os.path.exists(output_dir_sent):
        os.makedirs(output_dir_sent)
        
    for file in os.listdir(txt_files_sent):         
        if file.endswith("_sentiment.txt"): # checking if the file is a txt file
            file_path = os.path.join(txt_files_sent, file) # creating the
            file_name = os.path.basename(file_path).replace(".txt", "") # getting the name of the file without the extension
            output_path = os.path.join(output_dir_sent, file_name + ".json") # creating the output path for the json file and the json file
            
            data = extractor_sentiment(file_path) # extracting the data from the txt file (more details in the extractor function)
            write_as_json(data, output_path) # writing the data to the json file (more details in the write_as_json function)

def json_ner(txt_files_ner, output_dir_ner):
    if not os.path.exists(output_dir_ner):
        os.makedirs(output_dir_ner)
        
    # iterating through the files in the input directory and creating the json files for each of them    
    for file in os.listdir(txt_files_ner):
        if file.endswith("_ner.txt"): # checking if the file is a txt file
            file_path = os.path.join(txt_files_ner, file) # creating the
            file_name = os.path.basename(file_path).replace(".txt", "") # getting the name of the file without the extension
            output_path = os.path.join(output_dir_ner, file_name + ".json") # creating the output path for the json file and the json file
            
            data = extractor_named(file_path) # extracting the data from the txt file (more details in the extractor function)
            write_as_json(data, output_path) # writing the data to the json file (more details in the write_as_json function)
            
def main():
    # ****** IMPORTANT ******
    # input directory of the txt files with the NER and Sentiment Expressions
    # before running it, change the directories to fit your system
    # ****** IMPORTANT ******
    
    txt_files_sent = [#"/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Alice/Results/sentiment", 
                    #"/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Dracula/Results/sentiment",
                    "/Users/merterol/Desktop/VSCode/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Franky/Results/sentiment"
                    ]
    
    txt_files_ner = [#"/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Alice/Results/named",
                    #"/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Dracula/Results/named",
                    "/Users/merterol/Desktop/VSCode/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Franky/Results/named"
                    ]
    
    output_dir_sent = [#"/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Alice/json/sentiment",
                    #"/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Dracula/json/sentiment",
                    "/Users/merterol/Desktop/VSCode/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Franky/json/sentiment"
                    ]
    
    output_dir_ner = [#"/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Alice/json/named",
                    #"/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Dracula/json/named",
                    "/Users/merterol/Desktop/VSCode/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Franky/json/named"
                    ]
    
    # iterating through the txt files and creating the json files for each of them using the lists above
    for i in range(len(txt_files_sent)):
        json_sent(txt_files_sent[i], output_dir_sent[i])
        json_ner(txt_files_ner[i], output_dir_ner[i])
    
# This is the standard boilerplate that calls the main() function when the program is executed.
if __name__ == '__main__':
    main()
