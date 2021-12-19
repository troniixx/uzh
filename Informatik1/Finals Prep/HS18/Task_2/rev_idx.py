def rev_idx(words):
    d = {}
    idx = 0

    for i in words:
        i = i.lower()
        if not i in d.keys():
            d[i] = []
        d[i].append(idx)
        idx += 1
    return d

assert rev_idx([]) == {}
assert rev_idx(["a","b"]) == {"a": [0], "b": [1]}
assert rev_idx(["a","B","A","aa"]) == {"a": [0, 2], "aa": [3], "b": [1]}