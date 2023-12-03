"""
PCL 1 Fall Semester 2023 - Course Project
Part 0: Book Selection
Students: <person 1>, <person 2>
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


def main():
    # Here you may add the neccessary code to call your functions, and all the steps before, in between, and after calling them.
    txt_files = "/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Alice/Results"
    #txt_files = "/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Dracula/Results"
    #txt_files = "/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Frankenstein/Results"
    
    output_dir = "/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Alice/json"
    #output_dir = "/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Dracula/json"
    #output_dir = "/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Frankenstein/json"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    for file in os.listdir(txt_files):
        if file.endswith(".txt"):
            file_path = os.path.join(txt_files, file)
            file_name = os.path.basename(file_path).replace(".txt", "")
            output_path = os.path.join(output_dir, file_name + ".json")
            
            with open(file_path, "r") as file:
                text = file.read()
                data = {"title": file_name, "text": text}
                write_as_json(data, output_path)        
        

# This is the standard boilerplate that calls the main() function when the program is executed.
if __name__ == '__main__':
    main()
