import string
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize

TEXT = "/Users/merterol/uzh/Computational Linguistics/Sem 2/ECL 2/Exercise 3/gpt_text.txt"

def tokenizer(txt):
    with open(txt, "r") as file:
        text = file.read()

    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    
    return words


def get_token_count(txt):
    words = tokenizer(txt)
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
            
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    for word, count in sorted_word_counts:
        print(f"{word}: {count}")
    
    return word_counts

def vector_creator(txt):
    words = tokenizer(txt)
    
    # Tokens and targets
    top_six = ["the", "of", "and", "their", "animal", "kingdom"]
    targets = ["animal kingdom", "adorable", "deadly"]
    
    # Initialize vectors
    vectors = {target: [0] * len(top_six) for target in targets}
    
    # Iterate through words to fill in the context vectors
    for i, word in enumerate(words):
        if word in top_six:
            for target in targets:
                target_words = target.split()
                # Check for presence of target words/phrases near the token
                if all(target_word in words[max(0, i-10):i+10] for target_word in target_words):
                    vectors[target][top_six.index(word)] += 1
    
    for target, vector in vectors.items():
        print(f"Context vector for '{target}': {vector}")

if __name__ == "__main__":
    get_token_count(TEXT)
    vector_creator(TEXT)