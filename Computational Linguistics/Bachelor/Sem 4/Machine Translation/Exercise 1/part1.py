from sacremoses import MosesTokenizer
mt = MosesTokenizer(lang='en')

print("Part 1:")

def reader(file):
    with open(file, "r") as f:
        text = f.read()
        tokens = mt.tokenize(text)
        return tokens
    
def get_ngrams(file, n):
    ngrams = []
    tokens = reader(file)
    for i in range(len(tokens) - n + 1):
        ngrams.append(tokens[i:i+n])
    return ngrams

def ngram_precision(hyp, ref, n):
    hyp_len = len(hyp)
    correct = []
    ngram_hyp = get_ngrams(hyp, n)
    ngram_ref = get_ngrams(ref, n)

    for ngram in ngram_hyp:
        if ngram in ngram_ref:
            correct.append(ngram)
                

    return len(correct) / hyp_len

