from feature_extraction import Document, FeatureExtractor, GermanFeatureExtractor, EnglishFeatureExtractor

# Document class tests

def test_document_loading():
    doc = Document('test.txt')
    assert doc.file_path == 'test.txt'
    assert doc.text == """In computer programming, a string is traditionally a sequence of characters, either as a literal constant or as some kind of variable. The latter may allow its elements to be mutated and the length changed, or it may be fixed (after creation). A string is generally considered as a data type and is often implemented as an array data structure of bytes (or words) that stores a sequence of elements, typically characters, using some character encoding. String may also denote more general arrays or other sequence (or list) data types and structures.

Depending on the programming language and precise data type used, a variable declared to be a string may either cause storage in memory to be statically allocated for a predetermined maximum length or employ dynamic allocation to allow it to hold a variable number of elements.

When a string appears literally in source code, it is known as a string literal or an anonymous string.[1]

In formal languages, which are used in mathematical logic and theoretical computer science, a string is a finite sequence of symbols that are chosen from a set called an alphabet."""

def test_document_repr():
    doc = Document('test.txt')
    assert repr(doc) == "Document('test.txt')"

def test_document_length():
    # The length of the document should be the number of characters in the text
    doc = Document('test.txt')
    assert len(doc) == 1118

def test_document_sorting():
    # Documents should be sorted based on their length
    doc1 = Document('test.txt')
    doc1.text = 'short text'
    doc2 = Document('test.txt')
    doc2.text = 'longer text'
    doc3 = Document('test.txt')
    doc3.text = 'longest text'
    assert sorted([doc2, doc1, doc3]) == [doc1, doc2, doc3]

# FeatureExtractor class tests

def test_feature_extractor():
    doc = Document('test.txt')
    extractor = FeatureExtractor()
    features = extractor.extract_features(doc)
    assert features == {
        'char_count': 1118,
        'alpha_ratio': 904 / 1118,
        'unique_chars_count': 39,
    }
    
def test_german_feature_extractor():
    doc = Document('test.txt')
    doc.text = "Hallo, können wir uns morgen treffen? ä ü  ae ue ö"
    extractor = GermanFeatureExtractor()
    features = extractor.extract_features(doc)
    assert features == {
        'char_count': 50,
        'alpha_ratio': 37 / 50,
        'unique_chars_count': 22,
        'umlaut_count': 6,
        'modal_count': 1
    }
    
def test_english_feature_extractor():
    doc = Document('test.txt')
    doc.text = "Hello, can we meet tomorrow?"
    extractor = EnglishFeatureExtractor()
    features = extractor.extract_features(doc)
    assert features == {
        'char_count': 28,
        'alpha_ratio': 22 / 28,
        'unique_chars_count': 14,
        'Cap_word_count': 1,
        'article_count': 0
    }