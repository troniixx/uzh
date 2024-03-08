from abc import ABC, abstractmethod

class TextAnalyzer(ABC):
    def __init__(self, text):
        self.text = text
        
    @abstractmethod
    def analyze(self):
        pass
    
class TokenCounter(TextAnalyzer):
    def __init__(self, text):
        super().__init__(text)
    
    def analyze(self):
        return len(self.text.split())

class VowelCounter(TextAnalyzer):
    def __init__(self, text):
        super().__init__(text)
    
    def analyze(self):
        return sum([1 for x in self.text if x in "aeiou"])

class UpperCaseConverter(TextAnalyzer):
    def __init__(self, text):
        super().__init__(text)
        
    def analyze(self):
        return self.text.upper()
    
if __name__ == "__main__":
    tc = TokenCounter("This is a test string")
    print(tc.analyze())
    
    vc = VowelCounter("This is a test string")
    print(vc.analyze())
    
    uc = UpperCaseConverter("This is a test string")
    print(uc.analyze())