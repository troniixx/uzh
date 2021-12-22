#fuck this shit, doesnt work
def intersperse(s, l):
    lst = list(s)
    res = ""
    for i in lst:
        res += i
        x  = 0
        res += l[x]
        x += 1
    return res

# DO NOT SUBMIT THE LINES BELOW!
assert intersperse("H", [',']) == "H"
assert intersperse("Hello", [',']) == "H,e,l,l,o"
assert intersperse("Hello", [',', '.']) == "H,e.l,l.o"
assert intersperse("Hello", ['', '.']) == "He.ll.o"
assert intersperse("Hello", ['-o-', '_o_']) == "H-o-e_o_l-o-l_o_o"
assert intersperse("Hello", [',', '.', '-']) == "H,e.l-l,o"