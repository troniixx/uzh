from abc import ABC, abstractmethod

class TextAnalyzer(ABC):
    def __init__(self, text):
        self.text = text
        
    @abstractmethod
    def analyze(self):
        pass
    
class TokenCounter(TextAnalyzer):
    def analyze(self):
        return len(self.text.split())

class VowelCounter(TextAnalyzer):
    def analyze(self):
        return sum([1 for x in self.text if x in "aeiou"])

class UpperCaseConverter(TextAnalyzer):
    def analyze(self):
        return self.text.upper()

def process_text(texts):
    results = []
    count = 0
    
    for text in texts:
        results.append([])
        results[count].append(TokenCounter(text).analyze())
        results[count].append(VowelCounter(text).analyze())
        results[count].append(UpperCaseConverter(text).analyze())
        count += 1

    return results
    
if __name__ == "__main__":
    texts = ["This is a test string", "This is another test string", "This is a third test string",
            "This is a fourth test string", "This is a fifth test string", "This is a sixth test string"]
    
    print(process_text(texts))
