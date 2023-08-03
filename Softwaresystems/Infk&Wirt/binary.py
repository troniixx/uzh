def binary(num):
    s = ""
    if num != 0:
        while num >= 1:
            if num % 2 == 0:
                s = s + "0"
                num = num/2
            else:
                s = s + "1"
                num = num/2
    else:
        s="0"

    return "".join(reversed(s))


print(binary(12))