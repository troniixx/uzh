def to_binary(number):
    binarynumber=""
    if (number!=0):
        while (number>=1):
            if (number %2==0):
                binarynumber=binarynumber+"0"
                number=number/2
            else:
                binarynumber=binarynumber+"1"
                number=(number-1)/2

    else:
        binarynumber="0"

    return "".join(reversed(binarynumber))

if __name__ == '__main__':
    print(to_binary(35))
    print("\n")
    print(bin(35))