def equal_texts(text1, text2):
    flag = False

    #check if the length of the two texts are the same
    if len(text1) == len(text2):
        #iterate through the first text and check if the character is in the second text
        for i in range(len(text1)):
            if text1[i] != text2[i]:
                flag = False
                break
            else:
                flag = True
                
    return flag
                
def distance(text1, text2):
    counter = 0
    
    #iterate through the first text and check if the character is in the second text
    #if not +1 the counter
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            counter += 1
            
    return counter

def no_common_character(text1, text2):
    flag = False
    
    #iterate through the first text and check if the character is in the second text
    # and change the flag accordingly and in the end return it
    for char in text1:
        if char in text2:
            flag = False
            break # if one is false, then the whole thing is false
        else:
            flag = True
            
    return flag

if __name__ == "__main__":
    print(equal_texts(["v", "i", "s", "a"], ["v", "i", "s", "a"])) # should return True --> OK
    print(equal_texts(["v", "i", "s", "a"], ["v", "a", "i", "s"])) # should return False --> OK
    
    print(distance(["v", "i", "s", "a"], ["v", "a", "i", "s"])) # should return 3 --> OK
    print(distance(["a", "v", "i", "s"], ["v", "i", "s", "a"])) # shoudl return 4 --> OK
    
    print(no_common_character(["a", "v", "i", "s"], ["v", "i", "s", "a"])) # should return False --> OK
    print(no_common_character(["a", "v", "i", "s"], ["u", "r", "n", "e"])) # should return True --> OK
    