import ijson, sys
from lxml import etree as ET
from datetime import datetime
import argparse
import logging
from tqdm import tqdm

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s", stream=sys.stdout)

def parse_json(file_path):
    return open(file_path, "rb")

def is_weekend(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    return date_obj.weekday() in [5, 6]  # Saturday or Sunday

def create_xml_review(review):
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

def convert_to_xml(input_file, output_file):
    file = parse_json(input_file)
    reviews = tqdm(ijson.items(file, "item"), desc="Converting to XML")
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="utf-8"?>\n<root>')
        num_writes = 0
        for review in reviews:
            if is_weekend(review["date"]):
                xml_review = create_xml_review(review)
                f.write(xml_review)
                num_writes += 1
        f.write("</root>")
        
        return num_writes

def count_items(file_path):
    with parse_json(file_path) as file:
        return sum(1 for _ in ijson.items(file, "item"))

def main():
    parser = argparse.ArgumentParser(description="Convert JSON reviews to XML format.")
    parser.add_argument("-j", "--json_file", help="Path to the JSON file containing reviews", required=True)
    parser.add_argument("-x", "--xml", help="Filename for the outputted XML file", required=True)
    
    args = parser.parse_args()
    num_writes = convert_to_xml(args.json_file, args.xml)

    logging.info(f"Processed {count_items(args.json_file)} reviews from file {args.json_file}")
    logging.info(f"Written {num_writes} reviews to {args.xml}")
    

if __name__ == "__main__":
    main()

    """
    review.json:
        Converting to XML: 17it [00:00, 572.75it/s]
        INFO:root:Processed 17 reviews from file review.json
        INFO:root:Written 6 reviews to output_cli.xml
        
    review_large.json:
        Converting to XML: 6990280it [04:55, 23666.40it/s]
        INFO:root:Processed 6990280 reviews from file review_large.json
        INFO:root:Written 2211365 reviews to output_cli_large.xml
        
        Run 1: Memory Usage: 16.98 MB
        Run 2: Memory Usage: 16.914 MB
        
    """