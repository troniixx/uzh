#works
def calc(expression):
    lst = expression.split()
    
    if lst[0] == "+":
        return float(lst[1])+float(lst[2])
    if lst[0] == "-":
        return float(lst[1])-float(lst[2])
    if lst[0] == "*":
        return float(lst[1])*float(lst[2])
    if lst[0] == "/":
        if float(lst[2]) == 0:
            raise ValueError
        else: return float(lst[1]) / float(lst[2])

# DO NOT SUBMIT THE LINES BELOW!
assert calc("+ 1 2") == 3
assert calc("- 1 2") == -1
assert calc("* 1 2") == 2
assert calc("/ 1 2") == 0.5
assert calc("* 1 -2") == -2
assert calc("* 10.5 2") == 21
assert calc("* -10.5 -2") == 21