# -*- coding: utf-8 -*-
# Author: Mert Erol, 20-915-245

##### YOU CAN ADD IMPORTS HERE #####
import spacy
import string
from os.path import basename
####################################

class Document:
    """
    Represents a document, storing a text.
    """

    def __init__(self, file_path: str):
        """
        Initializes a new instance of Document.

        Args:
            file_path (str): The path to the document file.
        """
        self.file_path = basename(file_path) # The name of the file
        
        with open(file_path, "r", encoding="utf-8") as file:
            self.text = file.read() # Text extracted from the file -- DONE: implement its extraction
            
    # DONE: Implement loading text from file, and other functionalities as required
    
    #outputs the file name
    def __repr__(self) -> str:
        return f"Document('{self.file_path}')"
    
    #outputs the length of the text
    def __len__(self) -> int:
        return len(self.text)
    
    #used for comparisons to then sort the documents based on their length
    def __lt__(self, other: "Document") -> bool:
        return len(self.text) < len(other.text)

####################################

class FeatureExtractor:
    """
    Base class for extracting features from a document.
    
    This class should be subclassed to create specific feature extractors for different languages or requirements.
    """

    def extract_features(self, document: Document) -> dict[str, float]:
        """
        Extracts features from a document. This method should be overridden in subclasses.

        Args:
            document (Document): The document from which to extract features.

        Returns:
            Dict[str, float]: A dictionary containing the extracted features.
        """
        # Placeholder for base feature extraction logic. Implement feature extraction methods below.
        features = {
            'char_count': self._char_count(document.text),
            'alpha_ratio': self._alpha_ratio(document.text),
            'unique_chars_count': self._unique_chars_count(document.text),
        }
        return features

    # Methods for feature extraction:

    @staticmethod
    def _char_count(text: str) -> int:
        """
        Counts the number of characters in the specified text.
        
        Args:
            text (str): The text from which to count characters.

        Returns:
            int: The number of characters in the text.
        """
        # DONE: Implement this method to count characters in the text
        return len(text)

    @staticmethod
    def _alpha_ratio(text: str) -> float:
        """
        Calculates the ratio of characters that are alphabetic in the specified text.
        Alphabetic characters include letters (including umlauts etc.) but not numbers or punctuation.
        
        Args:
            text (str): The text from which to calculate alphabetic ratio.

        Returns:
            float: The ratio of alphabetic characters in the text.
        """
        # DONE: Implement this method to calculate the alphanumeric ratio
        if len(text) == 0: return 0.0
                
        alchars = sum([1 for c in text if c.isalpha()])
        
        return float(alchars / len(text))

    @staticmethod
    def _unique_chars_count(text: str) -> float:
        """
        Counts the number of unique characters in the specified text.
        
        Args:
            text (str): The text from which to count the unique characters.

        Returns:
            float: The number of unique characters in the text.
        """
        # DONE: Implement this method to count unique characters
        return float(len(set(text)))


###### DONE: YOUR FEATURE EXTRACTOR IMPLEMENTATIONS HERE ######
class GermanFeatureExtractor(FeatureExtractor):
    def umlaut_count(self) -> int:
        #list comprehensions didnt work so i did it the usual way
        count = 0
        uml = ["ä", "ö", "ü", "ae", "oe", "ue"]
        
        #iterate through the umlauts and count them in the text
        for u in uml:
            count += self.text.lower().count(u)
        
        #return the count
        return count
        
    def modal_count(self) -> int:
        #remove punctuation to make it easier to count the modals
        text = ''.join(char for char in self.text if char not in string.punctuation)
        #count the modals
        return len([word for word in text.split() if word.lower() in ["können", "müssen", "sollen", "wollen", "dürfen", "mögen"]])

class EnglishFeatureExtractor(FeatureExtractor):
    def cap_word_count(self) -> int:
        #remove punctuation
        text = ''.join(char for char in self.text if char not in string.punctuation)
        #count the words that start with a capital letter and are longer than 1 character
        return len([word for word in text.split() if word[0].isupper() and len(word) > 1])
    
    def article_count(self) -> int:
        #remove punctuation
        text = ''.join(char for char in self.text if char not in string.punctuation)
        #count the articles
        return len([word for word in text.split() if word.lower() in ["a", "an", "the"]])
