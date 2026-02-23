def foo(w, s):
    """Returns the index of the first occurrence of s in w, or -1 if s is not in w."""
    try:
        #try to find the index of s in w
        return w.index(s) #return the index of the first occurrence of s in w
    except ValueError: #if s is not in w, index raises a ValueError
        return -1 #return -1 instead
    
if __name__ == "__main__":
    print(foo("hello", "l"))
    print(foo("hello", "a"))
    print(foo(12, 2))
    