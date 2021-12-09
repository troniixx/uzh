sentence = "The quick brown fox jumps over the lazy dog"
print(sentence[0:3])
print(sentence[-8:])

print((9 ** 2 - 4 ** 3 + 8) ** 0.5)


account_stm = "The balance of account no. %s is %.4f"
print(account_stm % ("CH123 888 222", 123.225))


def fun(n):
    if n > 0:
        return "x"
print(type(17), type(3.1415), type(fun), type(fun(5)), type(fun(-2)))