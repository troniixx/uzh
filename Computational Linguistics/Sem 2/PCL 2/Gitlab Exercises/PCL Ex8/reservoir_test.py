import ijson
import sys
from lxml import etree as ET
from datetime import datetime
import argparse
import logging
from tqdm import tqdm
from typing import Dict, Tuple, List
import random

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s", stream=sys.stdout)

def parse_json(file_path: str) -> ijson.common.items:
    """
    Open and parse the JSON file as a binary stream.
    
    Args:
        file_path (str): The path to the JSON file.
    
    Returns:
        ijson.common.items: An iterator over items in the JSON file.
    """
    return open(file_path, "rb")

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

def create_xml_review(review: Dict[str, str]) -> str:
    """
    Create an XML representation of a review.
    
    Args:
        review (Dict[str, str]): A dictionary containing review data.
    
    Returns:
        str: The XML string representation of the review.
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
    
    return ET.tostring(review_elem, pretty_print=True, encoding="unicode")

def reservoir_sampling(iterator, k: int) -> List[Dict[str, str]]:
    """
    Perform reservoir sampling on an iterator.
    
    Args:
        iterator: An iterator over the items.
        k (int): The number of items to sample.
    
    Returns:
        List[Dict[str, str]]: A list containing the sampled items.
    """
    reservoir = []
    for i, item in enumerate(iterator):
        if i < k:
            reservoir.append(item)
        else:
            j = random.randint(0, i)
            if j < k:
                reservoir[j] = item
    return reservoir

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
    file = parse_json(input_file)
    reviews = ijson.items(file, "item")
    
    reservoir = []
    train_count = 0
    test_count = 0
    
    with open(train_file, "w", encoding="utf-8") as train_f, open(test_file, "w", encoding="utf-8") as test_f:
        train_f.write('<?xml version="1.0" encoding="utf-8"?>\n<root>')
        test_f.write('<?xml version="1.0" encoding="utf-8"?>\n<root>')
        
        for review in tqdm(reviews, desc="Processing reviews"):
            if is_weekend(review["date"]):
                xml_review = create_xml_review(review)
                if len(reservoir) < n:
                    reservoir.append(xml_review)
                else:
                    j = random.randint(0, train_count + test_count)
                    if j < n:
                        train_f.write(reservoir[j])
                        reservoir[j] = xml_review
                        train_count += 1
                    else:
                        train_f.write(xml_review)
                        train_count += 1
        
        for xml_review in reservoir:
            test_f.write(xml_review)
            test_count += 1
        
        train_f.write("</root>")
        test_f.write("</root>")
    
    return train_count, test_count

def count_items(file_path: str) -> int:
    """
    Count the number of items in a JSON file.
    
    Args:
        file_path (str): The path to the JSON file.
    
    Returns:
        int: The number of items in the JSON file.
    """
    with parse_json(file_path) as file:
        return sum(1 for _ in ijson.items(file, "item"))

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
