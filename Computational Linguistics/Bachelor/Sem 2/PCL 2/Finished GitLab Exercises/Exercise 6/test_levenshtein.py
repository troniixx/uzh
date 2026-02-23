# Student Name: Mert Erol
# Matriculation Number: 20-915-245
# Environment: Python 3.12.3
# Encoding: UTF-8

from unittest.mock import mock_open, MagicMock, patch
from levenshtein_base import levenshtein, argument_processor
from levenshtein_cli import main, create_parser, float_or_int
import pytest, argparse
import io, sys

# **** START Tests for levenshtein_base.py ****

def test_equal_weights():
    s1 = ["In", "the", "heart", "of", "the", "bustling", "city", "the", "library", "stood", "as", "a", "center", "of", "learning", "its", "walls", "lined", "with", "books", "that", "whispered", "secrets", "of", "the", "past", "to", "those", "who", "listened", "closely"] 
    s2 = ["In", "the", "heart", "of", "the", "bustling", "city", "the", "ancient", "library", "stood", "as", "a", "beacon", "of", "knowledge", "its", "walls", "lined", "with", "books", "that", "whispered", "secrets", "from", "the", "past", "to", "those", "who", "listened"]

    distance = levenshtein(s1, s2, insertion_cost=1,
                            deletion_cost=1, substitution_cost=1)
    assert distance == 5

    s1 = "In the heart of the bustling city, the library stood as a center of learning, its walls lined with books that whispered secrets of the past to those who listened closely."
    s2 = "In the heart of the bustling city, the ancient library stood as a beacon of knowledge, its walls lined with books that whispered secrets from the past to those who listened"

    distance = levenshtein(s1, s2, insertion_cost=1,
                            deletion_cost=1, substitution_cost=1)
    assert distance == 33


def test_expensive_substitution():
    s1 = ["In", "the", "heart", "of", "the", "bustling", "city", "the", "library", "stood", "as", "a", "center", "of", "learning", "its", "walls", "lined", "with", "books", "that", "whispered", "secrets", "of", "the", "past", "to", "those", "who", "listened", "closely"] 
    s2 = ["In", "the", "heart", "of", "the", "bustling", "city", "the", "ancient", "library", "stood", "as", "a", "beacon", "of", "knowledge", "its", "walls", "lined", "with", "books", "that", "whispered", "secrets", "from", "the", "past", "to", "those", "who", "listened"]

    distance = levenshtein(s1, s2, insertion_cost=1,
                            deletion_cost=1, substitution_cost=12)
    assert distance == 8

    s1 = "In the heart of the bustling city, the library stood as a center of learning, its walls lined with books that whispered secrets of the past to those who listened closely."
    s2 = "In the heart of the bustling city, the ancient library stood as a beacon of knowledge, its walls lined with books that whispered secrets from the past to those who listened"

    distance = levenshtein(s1, s2, insertion_cost=1,
                            deletion_cost=1, substitution_cost=12)
    assert distance == 40


def test_cheap_substitution():
    s1 = "Today, we're excited to launch our latest feature, designed to enhance user experience across our platform."
    s2 = "Today, we are excited to announce our latest feature, aimed at enhancing the user experience across the platform."

    distance = levenshtein(s1, s2, insertion_cost=1,
                            deletion_cost=1, substitution_cost=0.5)
    assert distance == 17

    s1 = ["Today", "we're", "excited", "to", "launch", "our", "latest", "feature", "designed", "to", "enhance", "user", "experience", "across", "our", "platform"] 
    s2 = ["Today", "we", "are", "excited", "to", "announce", "our", "latest", "feature", "aimed", "at", "enhancing", "the", "user", "experience", "across", "the", "platform"]

    distance = levenshtein(s1, s2, insertion_cost=1,
                            deletion_cost=1, substitution_cost=0.5)
    assert distance == 5

def test_empty_string():
    s1 = ""
    s2 = ""
    distance = levenshtein(s1, s2, insertion_cost=1,
                            deletion_cost=1, substitution_cost=1)
    
    assert distance == 0

def test_levenshtein_edge_cases():

    assert levenshtein("hello", "hello", 0, 0, 0, False) == 0
    assert levenshtein("", "", 1, 1, 1, False) == 0


def test_exact_copies():
    s1 = "Hello, world!"
    s2 = "Hello, world!"
    distance = levenshtein(s1, s2, insertion_cost=1,
                            deletion_cost=1, substitution_cost=1)
    assert distance == 0
    
    s1 = ["Hello", "world"]
    s2 = ["Hello", "world"]
    
    distance = levenshtein(s1, s2, insertion_cost=1,
                            deletion_cost=1, substitution_cost=1)
    
    assert distance == 0
    
def test_one_empty():
    s1 = "Hello, world!"
    s2 = ""
    distance = levenshtein(s1, s2, insertion_cost=1,
                            deletion_cost=1, substitution_cost=1)
    
    assert distance == 13
    
    s1 = ["Hello", "world"]
    s2 = []
    distance = levenshtein(s1, s2, insertion_cost=1,
                            deletion_cost=1, substitution_cost=1)
    assert distance == 2

def test_tokenize_true():
    s1 = "Hello, world!"
    s2 = "Hello world!"
    distance = levenshtein(s1, s2, insertion_cost=1,
                            deletion_cost=1, substitution_cost=1, tokenize=True)
    
    assert distance == 0    

def test_argument_processor_errors():
    with pytest.raises(ValueError) as excinfo:
        argument_processor("hello", "world", "one", "two", "three", False)
    assert "must be numbers" in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        argument_processor("hello", "world", -1, -1, -1, False)
    assert "must be non-negative" in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        argument_processor(123, 456, 1, 1, 1, False)
    assert "must be strings or lists" in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        argument_processor("hello", "world", 1, 1, 1, "maybe")
    assert "must be a boolean" in str(excinfo.value)
    
def test_levenshtein_errors():
    with pytest.raises(ValueError):
        levenshtein("a", "b", insertion_cost="x", deletion_cost="y", substitution_cost="z", tokenize="n")

def test_different_number_of_lines():
    insertion_cost = 1
    deletion_cost = 1
    substitution_cost = 1
    
    s1 = ["In", "the", "heart", "of", "the", "bustling", "city", "the", "library", "stood", "as", "a", "center", "of", "learning", "its", "walls", "lined", "with", "books", "that", "whispered", "secrets", "of", "the", "past", "to", "those", "who", "listened", "closely"] 
    s2 = ["In", "the", "heart", "of", "the", "bustling", "city", "the", "ancient", "library", "stood", "as", "a", "beacon", "of", "knowledge", "its", "walls", "lined", "with", "books", "that", "whispered", "secrets", "from", "the", "past", "to", "those", "who", "listened", "closely"]
    
    with pytest.raises(ValueError):
        levenshtein(s1, s2, insertion_cost, deletion_cost, substitution_cost)
    
def test_invalid_arguments_type():
    a = 123
    b = "Hello"
    insertion_cost = 1
    deletion_cost = 1
    substitution_cost = 1
    
    with pytest.raises(ValueError):
        levenshtein(a, b, insertion_cost, deletion_cost, substitution_cost)
    
def test_tokenize():
    a = "Hello my name is Mert"
    b = "Hello my name was Mert"
    insertion_cost = 1
    deletion_cost = 1
    substitution_cost = 1
    tokenize = True
    
    result = levenshtein(a, b, insertion_cost, deletion_cost, substitution_cost, tokenize)
    
    assert result == 1
    
def test_negative_costs_insert():
    insertion_cost = -1
    deletion_cost = 0
    substitution_cost = 1
    
    with pytest.raises(ValueError):
        levenshtein(["a"], ["a"], insertion_cost, deletion_cost, substitution_cost)

def test_negative_costs_delete():
    insertion_cost = 1
    deletion_cost = -1
    substitution_cost = 1
    
    with pytest.raises(ValueError):
        levenshtein(["a"], ["a"], insertion_cost, deletion_cost, substitution_cost)

def test_negative_costs_substitute():        
    insertion_cost = 1
    deletion_cost = 1
    substitution_cost = -1
    
    with pytest.raises(ValueError):
        levenshtein(["a"], ["a"], insertion_cost, deletion_cost, substitution_cost)

def test_all_negative_costs():
    insertion_cost = -1
    deletion_cost = -1
    substitution_cost = -1
    
    with pytest.raises(ValueError):
        levenshtein(["a"], ["a"], insertion_cost, deletion_cost, substitution_cost)

def test_invalid_arguments_type():
    a = 123
    b = "Hello"
    insertion_cost = 1
    deletion_cost = 1
    substitution_cost = 1
    
    with pytest.raises(ValueError):
        levenshtein(a, b, insertion_cost, deletion_cost, substitution_cost)

def test_invalid_tokenize_value():
    a = "Hello"
    b = "World"
    insertion_cost = 1
    deletion_cost = 1
    substitution_cost = 1
    tokenize = 2
    
    with pytest.raises(ValueError):
        levenshtein(a, b, insertion_cost, deletion_cost, substitution_cost, tokenize)

# *** END Tests for levenshtein_base.py ***

# **** START Tests for levenshtein_cli.py ****

def test_argument_parsing(monkeypatch):
    args = ["prog", "-f1", "test1.txt", "-f2", "test2.txt", "-i", "1", "-d", "1", "-s", "1", "-t"]
    monkeypatch.setattr(sys, "argv", args)
    args = create_parser().parse_args()
    assert args.file1 == "test1.txt"
    assert args.file2 == "test2.txt"
    assert args.insertion == 1
    assert args.deletion == 1
    assert args.substitution == 1
    assert args.tokenize is True

def test_float_or_int():
    assert float_or_int("10") == 10
    assert float_or_int("10.5") == pytest.approx(10.5)
    with pytest.raises(argparse.ArgumentTypeError):
        float_or_int("invalid")

#chatgpt helped with this test
def test_line_by_line_distance_calculation(monkeypatch, capsys):
    test_data1 = "Hello, world!\nGood morning, world!"
    test_data2 = "Hello world\nGood evening, world."
    mock_file = mock_open(read_data=test_data1)
    mock_file().readlines = MagicMock(side_effect=[test_data1.split("\n"), test_data2.split("\n")])
    
    monkeypatch.setattr(sys, "argv", ["prog", "-f1", "file1.txt", "-f2", "file2.txt"])
    monkeypatch.setattr("builtins.open", mock_file)
    
    with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
        main()
        output = mock_stdout.getvalue()
        assert "Levenshtein distance between line " in output

def test_invalid_numeric_input(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["prog", "-f1", "file1.txt", "-f2", "file2.txt", "-i", "invalid"])
    with pytest.raises(SystemExit):
        create_parser().parse_args()

def test_main_cli_missing_args(capsys):
    with pytest.raises(SystemExit):
        sys.argv = ["prog"]
        main()
    captured = capsys.readouterr()
    assert "the following arguments are required" in captured.err

def test_main_read_files(monkeypatch, capsys):
    with patch("builtins.open", mock_open(read_data="line1\nline2")) as mock_file:
        sys.argv = ["prog", "-f1", "dummy.txt", "-f2", "dummy.txt"]
        main()
        assert mock_file.call_count == 2
        captured = capsys.readouterr()
        assert "Levenshtein distance between line" in captured.out

#chatgpt helped me here
def test_file_not_found(capsys):
    with patch("builtins.open", mock_open()) as mocked_open:
        mocked_open.side_effect = FileNotFoundError("File not found.")
        
        with pytest.raises(SystemExit) as exc_info:
            main()
        
        assert exc_info.value.code == 1
        captured = capsys.readouterr()
        assert "File not found. Exiting..." in captured.err
        
# **** END Tests for levenshtein_cli.py ****