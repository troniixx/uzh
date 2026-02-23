def tabulate_chars(str):
    d = {}
    s = str.lower()
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    
    sort_d = sorted(d.items(), key = lambda item: item[1], reverse=True)
    
    for key, val in sort_d:
        if key == " ":
            continue
        else:
            print(key, val)

if __name__ == '__main__':
    print(tabulate_chars("ottos mops trotzt"))