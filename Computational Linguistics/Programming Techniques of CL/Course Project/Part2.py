"""
PCL 1 Fall Semester 2023 - Course Project
Part 0: Book Selection
Students: Mert Erol, Andrea Scheck
"""
# --- Imports ---
import os
import re
import sys
import json
from collections import defaultdict
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

""" How I run this (on Ubuntu for Windows):
python3 Part2.py "/mnt/c/users/andre/Dropbox/Uni/Programmiertechniken/Exercises/Course Project/Part 0/Books/Alice/Chapters" "/mnt/c/users/andre/Dropbox/Uni/Programmiertechniken/Exercises/Course Project" "Alice"
python3 Part2.py [input path, where the chapters are] [output path, where to put the files] [Book name]
Be patient when running it, the sentiment analysis takes a moment.
"""

# --- Functions ---
output_file = ""

def grep_sentences(input_folder, output_folder, output_name):
    """
    This function applies a grep to all the chapter files we created in part 0.
    It gets all the sentences which contain a main character name and applies some small cleaning functions (see below).
    It runs the sentences through the sentiment analyzer function (also see below).
    You could run this grep over the entire cleaned book txt, but this way, we can easily keep the distinction of the chapters (useful later).
    """
    os.makedirs(output_folder, exist_ok=True)

    output_file = os.path.join(output_folder, f"{output_name}.txt")

    with open(output_file, 'a') as result_file: #open output file
        for filename in os.listdir(input_folder): #iterate over all files in the chapter folder
            file_path = os.path.join(input_folder, filename)

            with open(file_path, 'r') as file: #read them
                file_content = file.read()

            cleaned_before_grep = clean_text_before_grep(file_content) #apply the preclean
            print(f'Pre-Cleaned {filename}') #and tell us you did it so we have some progress indication

            sentence_pattern = r'([.]+[\s\w,\',;:"!?]*(Alice|Queen|King|Hatter|Van Helsing|Lucy|Mina|Jonathan|Elizabeth|Clerval|Justine|Victor)[\s\w,\']*[:;.?!]+)'
            sentence_matches = re.findall(sentence_pattern, cleaned_before_grep) #find sentences with main character names in them

            for sentence, main_character in sentence_matches:
                postprocessed_text = prepare_output_text(sentence, main_character, filename) #apply the postclean 
                sentiment_value = analyze_sentiment(postprocessed_text)
                print(f"Found & wrote match from {filename}")
                result_file.write(f"{postprocessed_text}; {sentiment_value}\n")

def clean_text_before_grep(input_text):
    """
    Cleans the input text before the grep:
    *Remove some formatting choices (e.g. \ and _)
    *Replace some stylistic choices we don't want to deal with in the grep (e.g. special quotation marks)
    """
    preprocessed_text = input_text.replace("\'", "'").replace('_', '').replace('’', "'").replace('“', '"').replace('”', '"').replace('--', ',')
    return preprocessed_text

def prepare_output_text(input_text, main_character, filename):
    """
    Prepares the output text after the grep for further work (and JSON conversion):
    *Remove some leftover leading sentence characters that are captured with the regex but don't belong to the actual sentence
    *Put a newline after each sentence
    *Join the lines if they belong to one singular sentence
    (These 2 are just for our benefit when we want to look at the file)
    *Extract the main character name and the file name you got the match from
    (This is important to use later when we write our findings to JSON)
    """
    postprocessed_lines = [re.sub(r'^[.?!\'"]+\s*', '', line) for line in input_text.split('\n')]
    text_with_name = f"{' '.join(postprocessed_lines)}; {main_character}"
    text_with_name_and_file = f"{text_with_name}; {filename.split('.')[0]}"
    return text_with_name_and_file

# Function to perform sentiment analysis
def analyze_sentiment(sentence):
    """
    This function runs the VADER analysis over the grepped sentences containing a main character name.
    """
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(sentence)['compound'] #we use the compound, so the exact value
    return sentiment_score

# --- Everything above this is saved in a txt file. The following function is applied to this file to create a JSON file. ---

# Function to save sentiment analysis results to a JSON file
def save_sentiment_results(output_file_path, output_folder, output_file_name):
    """
    This function extracts the information we want to put into the JSON file:
    *Name
    *Sentiment (as a float value so we can later calculate with it)
    *Chapter number
    """

    name_data = {}

    output_file_path = os.path.join(output_folder, f"{output_file_name}.txt")
    with open(output_file_path, 'r') as file:
        sentences = file.readlines()

    for sentence in sentences:
        matches = re.finditer(r'(Alice|Queen|King|Hatter|Van Helsing|Lucy|Mina|Jonathan|Elizabeth|Clerval|Justine|Victor); (chapter_\d+); (-?\d+\.\d+)', sentence)
        
        for match in matches:
            name = match.group(1)
            sentiment = float(match.group(3))  
            chapter_match = re.search(r'chapter_(\d+)', match.group(2))
            
            if chapter_match:
                chapter = chapter_match.group(1)

            entry = {"name": name, "sentiment": sentiment, "chapter": chapter}

            if name in name_data:
                name_data[name]["data"].append((entry["sentiment"], entry["chapter"]))
            else:
                name_data[name] = {"name": name, "data": [(entry["sentiment"], entry["chapter"])]}

    data = list(name_data.values())
    for entry in data:
        entry["data"] = sorted(entry["data"], key=lambda x: x[1])  # Sort by chapter
        entry["data"] = [f"{x[0]}; {x[1]}" for x in entry["data"]]

    output_info_file = os.path.join(output_folder, f"{output_file_name}_info.json")
    with open(output_info_file, 'w') as json_file:
        json.dump(data, json_file, indent=2)
        print('Wrote extracted info to: ' f"{output_file_name}_info.json")

    return data

def calculate_averages(output_data, output_folder, output_file_name):
    """
    This function is applied to the JSON file that was created to create a new JSON file.
    The new file contains the average sentiment values per person per chapter.
    """
    character_chapter_sum_count = defaultdict(lambda: defaultdict(lambda: {"sum": 0, "count": 0}))

    #Iterate through the extracted data
    for entry in output_data:
        name = entry["name"]
        data = entry["data"]

        for sentiment, chapter in [map(float, x.split("; ")) for x in data]:
            character_chapter_sum_count[name][chapter]["sum"] += sentiment
            character_chapter_sum_count[name][chapter]["count"] += 1

    #Calculate averages
    averages_data = []
    for character_name, character_data in sorted(character_chapter_sum_count.items()):
        character_entry = {"name": character_name, "averages": []}
        for chapter, data in sorted(character_data.items()):
            average = data["sum"] / data["count"] if data["count"] > 0 else 0
            character_entry["averages"].append({"chapter": int(chapter), "average": average})
        averages_data.append(character_entry)

    averages_file = os.path.join(output_folder, f"{output_file_name}_averages.json")
    with open(averages_file, 'w') as json_file:
        json.dump(averages_data, json_file, indent=2)
    print(f'Wrote averaged values per character per chapter to: {output_file_name}_averages.json')

    return averages_data

# Main function
def main():
    if len(sys.argv) != 4:
        print("How to use this module: python3 scriptname.py [folder path containing chapters] [output folder] [output file name]")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    output_file_name = sys.argv[3]

    # Make sure output_file is assigned properly
    output_file = os.path.join(output_folder, f"{output_file_name}.txt")

    grep_sentences(input_folder, output_folder, output_file_name)
    print('Grep of main character sentences done')
    print('Starting sentiment analysis, this will take a moment...')
    
    # Analyze sentiment for every grepped sentence in the output file
    with open(output_file, 'r') as grepped_file:
        grepped_sentences = grepped_file.readlines()
        for sentence in grepped_sentences:
            analyze_sentiment(sentence)
    print('Sentiment analysis done')

    # Extract info and write to JSON
    output_data = save_sentiment_results(output_file, output_folder, output_file_name)
    print('Extraction of name, chapter name, and sentiment value done')

    # Calculate averages and write to new JSON
    averages_data = calculate_averages(output_data, output_folder, output_file_name)
    print('Averaging sentiment values done')

# Run the main function
if __name__ == "__main__":
    main()