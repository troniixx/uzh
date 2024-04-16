# Student Name: Mert Erol
# Matriculation Number: 20-915-245
# Environment: Python 3.12.3, re 2023.8.8
# Encoding: UTF-8

import re

def error_check(a: str | list[str], b: str | list[str], insertion_cost: int | float, deletion_cost: int | float, substitution_cost: int | float, tokenize: bool | int) -> None | ValueError:
    """
    function to check for errors in the arguments passed to the levenshtein function and argument_processor
    :param a: str | list[str]
    :param b: str | list[str]
    :param insertion_cost: int | float
    :param deletion_cost: int | float
    :param substitution_cost: int | float
    :param tokenize: bool | int
    
    :raises ValueError: if any of the arguments are invalid
    """
    # error checking for arguments (type)
    if not all(isinstance(i, (int, float)) for i in [insertion_cost, deletion_cost, substitution_cost]):
        raise ValueError("Invalid arguments: insertion_cost, deletion_cost, and substitution_cost must be numbers")
    
    # error checking for arguments (non-negative)
    if any(i < 0 for i in [insertion_cost, deletion_cost, substitution_cost]):
        raise ValueError("Invalid arguments: insertion_cost, deletion_cost, and substitution_cost must be non-negative")
    
    # error checking for input (type)
    if not all(isinstance(i, (str, list)) for i in [a, b]):
        raise ValueError("Invalid arguments: a and b must be strings or lists")
    
    # error checking for tokenize (type)
    if tokenize not in [True, False, 1, 0]:
        raise ValueError("Invalid arguments: tokenize must be a boolean")

def argument_processor(a: str | list[str], b: str | list[str], *args, **kwargs) -> tuple[str | list[str], str | list[str], int | float, int | float, int | float] | int:
    """
    function to process the arguments passed to the levenshtein function and return them in a tuple for further processing if successful
    
    :param a: str | list[str]
    :param b: str | list[str]
    :param args: list
    :param kwargs: dict
    
    :return: tuple[str | list[str], str | list[str], int | float, int | float, int | float]
    """
    # keyword-argument processor (CLI) - if keyword arguments are passed
    insertion_cost = kwargs.get("insertion_cost")
    deletion_cost = kwargs.get("deletion_cost")
    substitution_cost = kwargs.get("substitution_cost")
    tokenize = kwargs.get("tokenize", False)
    
    # argument processor (CLI) - if NO keyword arguments are passed
    if len(args) == 4:
        insertion_cost, deletion_cost, substitution_cost, tokenize = args

    # Error Checking
    error_check(a, b, insertion_cost, deletion_cost, substitution_cost, tokenize)
    
    # tokenization (if tokenize is True)
    if tokenize and isinstance(a, str) and isinstance(b, str):
        # remove any punctuation besides apostrophes from contractions in both strings
        # got pattern from chatgpt
        a = re.sub(r"(?<!\w)[^\w\s'](?!\w)|(?<!\w)[^\w\s'](?=\w)|(?<=\w)[^\w\s'](?!\w)", "", a)
        b = re.sub(r"(?<!\w)[^\w\s'](?!\w)|(?<!\w)[^\w\s'](?=\w)|(?<=\w)[^\w\s'](?!\w)", "", b)

        # remove multiple whitespaces and split the strings
        a = re.sub(r"\s+", " ", a).strip()
        b = re.sub(r"\s+", " ", b).strip()
        a, b = a.split(), b.split()

    return a, b, insertion_cost, deletion_cost, substitution_cost

def levenshtein(a: str | list[str], b: str | list[str], *args, **kwargs) -> float | None:
    """
    function to calculate the Levenshtein distance between two strings or lists and return the distance if successful
    
    :param a: str | list[str]
    :param b: str | list[str]
    :param args: list
    :param kwargs: dict
    
    :return: float | None
    
    """
    # Get all arguments and process them (or raise an error if invalid)
    try:
        a, b, insertion_cost, deletion_cost, substitution_cost = argument_processor(a, b, *args, **kwargs)
    except ValueError as e:
        print(f"Error processing arguments: {e}\n Exiting...")
        raise
    
    # Matrix Initialization
    n, m = len(a), len(b)
    dp_matrix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    # Base Case: Cost for inserting characters into an empty "a" to match "b"
    for j in range(m + 1):
        dp_matrix[0][j] = j * insertion_cost
    # Base Case: Cost for deleting characters from "a" to match an empty "b"
    for i in range(n + 1):
        dp_matrix[i][0] = i * deletion_cost

    # Transitions
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i-1] == b[j-1]:
                dp_matrix[i][j] = dp_matrix[i-1][j-1]
            else:
                dp_matrix[i][j] = min(
                    dp_matrix[i-1][j] + insertion_cost,  # Insertion
                    dp_matrix[i][j-1] + deletion_cost,  # Deletion
                    dp_matrix[i-1][j-1] + substitution_cost  # Replacement

                )

    return dp_matrix[n][m]
