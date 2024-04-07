import re
import numpy as np

TEXT = "Computational Linguistics/Sem 2/ECL 2/Exercise 3/gpt_text.txt"
CTX = ["animal_kingdom", "deadly", "adorable"]

def process_text(txt):
    with open(txt, "r") as file:
        text = file.read()

    text = re.sub(r"animal kingdom", "animal_kingdom", text)
    text = re.sub(r"[-,.!?]", "", text)
    words = [word.lower() for word in text.split()]

    return words

def token_count(txt):
    cd = {}
    words = process_text(txt)

    for word in words:
        if word in cd:
            cd[word] += 1
        else:
            cd[word] = 1

    return sorted(cd.items(), key=lambda x:x[1], reverse = True)

# the function that embodies my lack of sleep and sanity
def vectorize(text):
    tokens = token_count(text) # get dict of tokens with count
    words = process_text(text) # get list of words
    v_animalkingdom, v_adorable, v_deadly = [0]*6, [0]*6, [0]*6 # initialize vectors for each context word
    top_six = [word[0] for word in tokens if word[0] not in CTX][:6] # top 6 tokens excluding context words
    positions = {ctx: [i for i, word in enumerate(words) if word == ctx] for ctx in CTX} # find positions of context words in text

    for i, token in enumerate(top_six): # iterate through top 6 tokens
        for ctx, pos_list in positions.items(): # iterate through context words
            for pos in pos_list: # iterate through positions of context words
                window = words[max(0, pos-5):min(len(words), pos+6)]  # list the 5 words before and after
                if token in window: # if token is in window
                    # increment the corresponding dimension of the corresponding vector
                    if ctx == "animal_kingdom": v_animalkingdom[i] += 1
                    elif ctx == "adorable": v_adorable[i] += 1
                    elif ctx == "deadly": v_deadly[i] += 1

    return v_animalkingdom, v_adorable, v_deadly

def magn(x):
    return np.sqrt(sum([i**2 for i in x]))

def cosine_sim(x, y):
    if magn(x) == 0 or magn(y) == 0:
        return 0  #for cases with zero magnitude
    return np.dot(x, y) / (magn(x) * magn(y))

if __name__ == "__main__":
    print(f"Token Count: {len(token_count(TEXT))}")
    print("6 most common tokens: ")
    print(token_count(TEXT)[:6])
    
    print("Vectors: ")
    v_animalkingdom, v_adorable, v_deadly = vectorize(TEXT)
    print("Animal Kingdom:", v_animalkingdom)
    print("Adorable:", v_adorable)
    print("Deadly:", v_deadly)
    
    print("Cosine Similarity: ")
    print(f"Similarity between animal_kingdom and adorable: {cosine_sim(v_animalkingdom, v_adorable)}")
    print(f"Similarity between animal_kingdom and deadly: {cosine_sim(v_animalkingdom, v_deadly)}")
