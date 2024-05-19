import sys
import ijson
import random
import logging
import argparse
from tqdm import tqdm
from lxml import etree as ET
from datetime import datetime
from typing import Dict, Tuple, List, Generator

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s", stream=sys.stdout)

def parse_json(file_path: str) -> Generator[Dict[str, str], None, None]:
    """
    Open and parse the JSON file as a binary stream.
    
    Args:
        file_path (str): The path to the JSON file.
    
    Returns:
        Generator[Dict[str, str], None, None]: A generator over items in the JSON file.
    """
    with open(file_path, "rb") as f:
        yield from ijson.items(f, "item")

def is_weekend(date_str: str) -> bool:
    """
    Check if a given date string falls on a weekend.
    
    Args:
        date_str (str): The date string in the format "%Y-%m-%d %H:%M:%S".
    
    Returns:
        bool: True if the date is a weekend, False otherwise.
    """
    date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    return date_obj.weekday() in [5, 6]  # Saturday or Sunday

def create_xml_review(review: Dict[str, str]) -> ET.Element:
    """
    Create an XML representation of a review.
    
    Args:
        review (Dict[str, str]): A dictionary containing review data.
    
    Returns:
        ET.Element: The XML element representation of the review.
    """
    review_elem = ET.Element("review")
    ET.SubElement(review_elem, "review_id").text = review["review_id"]
    ET.SubElement(review_elem, "user_id").text = review["user_id"]
    ET.SubElement(review_elem, "business_id").text = review["business_id"]
    
    ratings = ET.SubElement(review_elem, "ratings")
    ratings.set("stars", str(review["stars"]))
    ratings.set("useful", str(review["useful"]))
    ratings.set("funny", str(review["funny"]))
    ratings.set("cool", str(review["cool"]))
    
    ET.SubElement(review_elem, "text").text = review["text"]
    
    date = datetime.strptime(review["date"], "%Y-%m-%d %H:%M:%S")
    ET.SubElement(review_elem, "date", year=str(date.year), month=str(date.month), day=str(date.day), weekday=date.strftime("%A"))
    
    return review_elem

def process_reviews(input_file: str, n: int) -> Tuple[Generator[ET.Element, None, None], List[ET.Element]]:
    """
    Process reviews and perform reservoir sampling for the test set.
    
    Args:
        input_file (str): The path to the JSON input file.
        n (int): The number of items in the reservoir for the test set.
    
    Returns:
        Tuple[Generator[ET.Element, None, None], List[ET.Element]]: Generators for train and test reviews.
    """
    reviews = parse_json(input_file)
    reservoir = []
    train_reviews = []

    for review in reviews:
        if is_weekend(review["date"]):
            xml_review = create_xml_review(review)
            if n == 0:
                train_reviews.append(xml_review)
            else:
                if len(reservoir) < n:
                    reservoir.append(xml_review)
                else:
                    j = random.randint(0, len(train_reviews) + len(reservoir))
                    if j < n:
                        train_reviews.append(reservoir[j])
                        reservoir[j] = xml_review
                    else:
                        train_reviews.append(xml_review)

    return (review for review in train_reviews), reservoir

def write_xml(reviews: Generator[ET.Element, None, None], file_path: str) -> int:
    """
    Write reviews to an XML file.
    
    Args:
        reviews (Generator[ET.Element, None, None]): A generator of XML reviews.
        file_path (str): The path to the XML output file.
    
    Returns:
        int: The number of reviews written.
    """
    root = ET.Element("root")
    count = 0
    for review in reviews:
        root.append(review)
        count += 1
    tree = ET.ElementTree(root)
    tree.write(file_path, xml_declaration=True, encoding="utf-8", pretty_print=True)
    return count

def convert_to_xml(input_file: str, train_file: str, test_file: str, n: int) -> Tuple[int, int]:
    """
    Convert JSON reviews to XML format and write to train and test files using reservoir sampling.
    
    Args:
        input_file (str): The path to the JSON input file.
        train_file (str): The path to the XML train output file.
        test_file (str): The path to the XML test output file.
        n (int): The number of items in the reservoir for the test set.
    
    Returns:
        Tuple[int, int]: The number of reviews written to the train and test XML files.
    """
    train_reviews, reservoir = process_reviews(input_file, n)
    train_count = write_xml(train_reviews, train_file)
    test_count = write_xml((review for review in reservoir), test_file)
    return train_count, test_count

def count_items(file_path: str) -> int:
    """
    Count the number of items in a JSON file.
    
    Args:
        file_path (str): The path to the JSON file.
    
    Returns:
        int: The number of items in the JSON file.
    """
    return sum(1 for _ in parse_json(file_path))

def main() -> None:
    """
    Main function to parse arguments and convert JSON reviews to XML format.
    """
    parser = argparse.ArgumentParser(description="Convert JSON reviews to XML format.")
    parser.add_argument("-j", "--json_file", help="Path to the JSON file containing reviews", required=True)
    parser.add_argument("-t", "--xml_test", help="Filename for the outputted XML test file", required=True)
    parser.add_argument("-r", "--xml_train", help="Filename for the outputted XML train file", required=True)
    parser.add_argument("-n", "--reservoir_size", type=int, help="Number of items in the reservoir for the test set", required=True)
    
    args = parser.parse_args()
    train_count, test_count = convert_to_xml(args.json_file, args.xml_train, args.xml_test, args.reservoir_size)

    logging.info(f"Processed {count_items(args.json_file)} reviews from file {args.json_file}")
    logging.info(f"Written {train_count} reviews to {args.xml_train}")
    logging.info(f"Written {test_count} reviews to {args.xml_test}")

if __name__ == "__main__":
    main()
