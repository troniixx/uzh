import os
import subprocess
import sys

def convert_ipynb_to_pdf(notebook_path):
    # Check if the file exists and is a .ipynb file
    if not os.path.isfile(notebook_path) or not notebook_path.endswith('.ipynb'):
        print(f"Error: {notebook_path} is not a valid notebook file.")
        return
    
    # Build the nbconvert command
    command = f"jupyter nbconvert --to pdf {notebook_path}"
    
    try:
        # Execute the command
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully converted {notebook_path} to PDF.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during conversion: {e}")

if __name__ == "__main__":
    # Check if the script is given an argument for the notebook file path
    if len(sys.argv) != 2:
        print("Usage macOS: python3 notebook_to_pdf.py <path_to_notebook.ipynb>\nUsage Windows: python notebook_to_pdf.py <path_to_notebook.ipynb>")
    else:
        notebook_file = sys.argv[1]
        convert_ipynb_to_pdf(notebook_file)
