#-- THIS LINE SHOULD BE THE FIRST LINE OF YOUR SUBMISSION! --#

def censor(text, censored_words):
    words = text.split()
    res = []

    for word in words:
        alpha = "".join(e for e in word if e.isalpha())
        #print(alpha) #just for testing
        if alpha.lower() in censored_words:
            w = ""
            for c in word:
                if c.isalpha(): w += "#"
                else: w += c
            res.append(w)
        else: res.append(word)    
                
    
    
    return " ".join(res)

#-- THIS LINE SHOULD BE THE LAST LINE OF YOUR SUBMISSION! ---#

### DO NOT SUBMIT THE FOLLOWING LINES!!! THESE ARE FOR LOCAL TESTING ONLY!
assert(censor("Hello, World!", ["hello"])
    == "#####, World!")
assert(censor("Everything is going to be fine!", ["everything", "fine"])
    == "########## is going to be ####!" )
assert(censor("", ["does", "not", "matter"])
    == "")
assert(censor("Everything is going to be fine!", [])
    == "Everything is going to be fine!")