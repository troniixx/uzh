import sys
import nltk
from nltk.tokenize import word_tokenize

def main():
    """
    The main function of the program. It reads the text from a file, tokenizes it, and prints the total number of tokens and the most frequent token.

    The file path is provided as a command-line argument. If the file is not found, the program prints an error message and exits.    
    """
    try:
        with open(sys.argv[1], "r") as file:
            text = file.read()
    except IndexError:
        print("Please provide the file name as an argument.")
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)

    # Tokenizing the text
    tokens = tokenize(text)

    # Counting total number of tokens
    token_count = len(tokens)
    print(f"The document contains {token_count} tokens.")

    # Counting the most frequent token
    most_frequent_token = count_most_frequent_token(tokens) # Call for the function you're about to implement
    print(f"The most frequent token is '{most_frequent_token}'.")

def tokenize(text: str) -> list[str]:
    """
    Tokenizes the given text.

    Args:
    text (str): The text to tokenize.

    Returns:
    list[str]: A list of tokens from the text.
    """

    # Using NLTK to tokenize
    tokens = word_tokenize(text)

    return tokens


def count_most_frequent_token(tokens: list[str]) -> str:
    """
    Counts the most frequent token in the given list of tokens.

    Args:
    tokens (list[str]): A list of tokens from the text.

    Returns:
    str: The most frequent token.
    """
    # TODO: Implement the logic to find the most frequent token in the list 'tokens'

    return max(tokens, key = tokens.count) # Placeholder for the return value

if __name__ == "__main__":
    main()
