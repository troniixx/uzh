def recursive_reverse(s):
    if s == "": return ""

    return s[-1] + recursive_reverse(s[:-1])


if __name__ == '__main__':
    print(recursive_reverse("hello daddy"))