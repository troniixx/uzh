#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# readability_analysis.py

# University of Zurich
# Department of Computational Linguistics


import spacy
from pyphen import Pyphen
from abc import ABC, abstractmethod

class TextMetricsAnalyzer:
    """
    Class to analyze text metrics such as average sentence length, average syllables per word, and percentage of complex words.
    """
    def __init__(self):
        try:
            # Try loading the English language model for Spacy
            self._nlp = spacy.load("en_core_web_sm")
        except OSError as e:
            print("Error: Unable to load the spaCy model.")
            print("Please download the English language model using the following command:")
            print("python -m spacy download en_core_web_sm")
            raise e

        # Initialize Pyphen for syllable counting
        self._dic = Pyphen(lang='en')

    def calculate_text_metrics(self, text: list[str]) -> tuple[float, float, float]:
        num_sentences = 0
        num_words = 0
        num_syllables = 0
        num_complex_words = 0

        for line in text:
            if not line:
                continue
            doc = self._nlp(line)
            num_sentences += len(list(doc.sents))

            for token in doc:
                if not token.is_punct:
                    num_words += 1
                    syllables = len(self._dic.inserted(token.text).split("-"))
                    num_syllables += syllables
                    if syllables > 2:
                        num_complex_words += 1

        if num_sentences == 0 and num_words == 0:
            raise ValueError("The input file is empty. Please provide a non-empty file.")

        avg_sentence_len = num_words / num_sentences
        avg_syllables_per_word = num_syllables / num_words
        pct_complex_words = num_complex_words / num_words

        return (avg_sentence_len, avg_syllables_per_word, pct_complex_words)


class ReadabilityIndex(ABC):
    """
    Abstract base class for readability indices.
    """
    @abstractmethod
    def calculate(self, metrics: tuple[float, float, float]) -> float:
        pass

    @abstractmethod
    def interpret(self, index_value: float) -> str:
        pass

    def calculate_and_interpret(self, metrics: tuple[float, float, float]) -> tuple[float, str]:
        index_value = self.calculate(metrics)
        interpretation = self.interpret(index_value)
        return index_value, interpretation


class FleschKincaidGradeLevel(ReadabilityIndex):
    """
    Implementation of the Flesch-Kincaid Grade Level readability index.
    """
    def calculate(self, metrics: tuple[float, float, float]) -> float:
        avg_sentence_len, avg_syllables_per_word, _ = metrics
        index_value = round(0.39 * avg_sentence_len + 11.8 * avg_syllables_per_word - 15.59, 3)
        return index_value
    
    def interpret(self, index_value: float) -> str:
        if index_value <= 1:
            return "Basic level for those who just learn to read books."  
        elif 1 < index_value <= 5:
            return "Very easy to read."
        elif 5 < index_value <= 11:
            return "Average level. Good for the majority of marketing materials."
        else:
            return "The text is for skilled readers. For example, an academic paper."


class GunningFogIndex(ReadabilityIndex):
    """
    Implementation of the Gunning Fog Index readability index.
    """
    def calculate(self, metrics: tuple[float, float, float]) -> float:
        avg_sentence_len, _, pct_complex_words = metrics
        index_value = round(0.4 * (avg_sentence_len + 100 * pct_complex_words), 3)
        return index_value
    
    def interpret(self, index_value: float) -> str:
        if index_value <= 1:
            return "Basic level for those who just learn to read books."  
        elif 1 < index_value <= 5:
            return "Very easy to read."
        elif 5 < index_value <= 8:
            return "A text is considered ideal for average readers."
        elif 8 < index_value <= 11:
            return "Fairly difficult to read."
        else:
            return "Too hard to read for the majority of readers."