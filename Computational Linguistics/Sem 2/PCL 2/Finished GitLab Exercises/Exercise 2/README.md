[![pipeline status](../../../badges/master/pipeline.svg)](../../../-/pipelines)
[![pipeline status](../../../badges/master/coverage.svg)](../../../-/pipelines)

(You **don't** need to reach 100% test coverage in this exercise.)

# PCL 2 Exercise 2: Authorship Analysis Toolkit

## Introduction
This exercise is an application of object-oriented programming (OOP) principles in Python, aimed at building a comprehensive authorship analysis toolkit. This toolkit is designed to process documents from various file formats, detect the language of the text, and extract specific textual features to construct an authorship signature.

The provided starter code includes the classes `Document` and `FeatureExtractor`, which you will need to complete. You will also need to implement two language specific `FeatureExtractor` subclasses. 

### Evaluation Criteria
This exercise is part of the course assessment and will contribute one point towards your final grade. Ensure you adhere to the following to achieve full marks:
- Independent completion of the exercise.
- Functional implementation that aligns with OOP principles.
- Proper use and application of specified Python constructs and patterns.

**Note that a passing unit tests is not sufficient for getting full marks.**

### Submission
**This is a graded exercise.** Submit your exercise through GitLab by **March 12th at 23:59**. Late submissions will result in zero points. Fork the exercise repository to start, and remember to include your name and matriculation number in all files. Set up your GitLab account to add tutors as 'Reporters' and finalize your submission by creating a release. Consult the `instructions.pdf` in OLAT for detailed submission guidelines.

### Important Notes
- Retain the provided directory structure and code templates.
- Do not alter predefined function and class signatures. We have written some tests to help you. If your implementation of the base classes is correct, you should pass all tests.
- Enhance your code's understandability with relevant comments and docstrings.

## Exercise Tasks

### Task 1: `Document` Class

- Complete the `Document` class to handle text extraction. Ensure your class can read documents from files and store their content for analysis.
- Define special methods in the `Document` class to implement the functionality defined in the unit tests.

### Task 2: `FeatureExtractor` Class

Finish implementing the language-independent `FeatureExtractor` class by completing the TODOs. Refer to the unit tests to check your implementations.

### Task 3: Language-Specific Subclasses

Create and implement subclasses of `FeatureExtractor` for at least **two distinct languages** with at least **two features each**. These should extend the base functionality to cater to specific linguistic traits and rules of the languages chosen. For instance, if you choose English and German, your feature extractors should reflect unique characteristics pertinent to English and German texts, respectively. You may use different sets of language-specific features for the two languages. Feel free to get creative, and refer to Appendix B for inspiration. You are allowed (but not required) to use additional libraries such as spaCy to implement your features.

These subclasses should **have the same public interface as the parent class** and **reuse as much code as possible from the parent class**. Refer to Appendix A for example usage.

You are not required to write unit tests for this task, but it might make it easier for you to check your implementation. Document your code with docstrings (and comments if necessary).

## Appendix A: Example Usage and Expected Output

For the expected output of the `Document` and `FeatureExtractor` classes, refer to the unit tests.

Here is an example output for a language-specific English feature extractor:
```python
# Assuming 'sample_document.txt' contains English text.
document = Document('sample_document.txt')
extractor = EnglishFeatureExtractor()
features = extractor.extract_features(document)
print(features)

# Output example:
{
    # Language-independent features:
    'char_count': 150,
    'alpha_ratio': 0.92,
    'unique_chars_ratio': 0.8,
    # Language-dependent features (yours may differ):
    'common_word_frequency': 0.43,
    ...  # more features
}
```

## Appendix B: Examples for Language-Specific Features
In this exercise, each language-specific subclass of FeatureExtractor should implement at least two unique features reflective of the linguistic characteristics inherent to the language it analyzes. Here are some suggested features for English, German, Italian, and French. These should serve as inspiration, you can implement any of the following but should also feel free to implement your own ideas.

### English
- Capitalized Words Count: Count the number of words starting with a capital letter, useful for identifying proper nouns or sentence beginnings.
- Modal Verbs Frequency: Calculate the frequency of English modal verbs (e.g., 'can', 'could', 'may', 'might', 'must', 'shall', 'should', 'will', 'would').
- Article Frequency: Count the occurrences of definite and indefinite articles ('the', 'a', 'an').
- Common Conjunctions: Measure the frequency of common English conjunctions (e.g., 'and', 'but', 'or', 'so', 'for', 'nor', 'yet').
- ...

### German
- Umlaut Words Count: Count the number of words containing umlauts (ä, ö, ü).
- Modal Verbs Frequency: Calculate the frequency of German modal verbs (e.g., 'dürfen', 'können', 'mögen', 'müssen', 'sollen', 'wollen').
- Sentence Structure Complexity: Measure the complexity of sentences by counting the average number of clauses per sentence.
- Article Frequency: Count the occurrences of articles ('der', 'die', 'das', etc).
- ...

### Italian
- Clitic Pronouns Count: Count the number of clitic pronouns (e.g., 'mi', 'ti', 'si', 'ci', 'vi', 'lo', 'la', 'li', 'le', 'ne').
- Definite Article Forms: Count the occurrences of definite articles (il, lo, la, i, gli, le).
- Conjunction Frequency: Measure the frequency of conjunctions (e.g., 'e', 'ma', 'anche', 'perché', 'se').
- Reflexive Verbs Count: Count occurrences of reflexive verbs, indicating reflexive actions or states.
- ...

### French
- Liaison Occurrences: Identify and count occurrences of liaisons, a phonetic feature connecting adjacent words.
- Negation Forms: Track the usage of different negation forms ('ne...pas', 'ne...plus', 'ne...jamais').
- Partitive Article Forms: Count occurrences of partitive articles ('du', 'de la', 'des'), indicative of partitive aspect.
- Verb Conjugation Variety: Analyze the diversity of verb conjugations used, reflecting verbal complexity.
- ...

### etc.
