class BTP():
    def __init__(self, str):
        self.text = str
        
    def lc_text(self):
        return self.text.lower()
    
    def wc(self):
        return len(self.text.split())
    
class ATP(BTP):
    def __init__(self, str, sw):
        super().__init__(str)
        self.sw = sw
        
    def wc(self):
        return  len([x for x in self.text.split() if x not in self.sw])
    
    def unique_word(self):
        return len(set(self.text.split()))
        

if __name__ == "__main__":
    sw = ["the", "is", "at", "which", "on"]
    
    print("BTP")
    btp = BTP("This is a test string This is a test string")
    print(btp.lc_text())
    print(btp.wc())
    
    print("\nATP")
    atp = ATP("This is a test string This is a test string", sw)
    print(atp.lc_text())
    print(atp.wc())
    print(atp.unique_word())