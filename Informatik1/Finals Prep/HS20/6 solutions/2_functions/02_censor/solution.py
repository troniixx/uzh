#!/usr/bin/env python3

def censor(text, censored_words):
    words = text.split()
    res = []
    for word in words:
        alpha_only = ''.join(e for e in word if e.isalpha())
        if alpha_only.lower() in censored_words:
            w = ""
            for c in word:
                if c.isalpha():
                    w += "#"
                else:
                    w += c
            res.append(w)
        else:
            res.append(word)
    return " ".join(res)

