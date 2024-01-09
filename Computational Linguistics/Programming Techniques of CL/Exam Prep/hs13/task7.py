def trunk(l: list, n: int) -> list:
    """Shortens strings in the list to length n"""
    sol = []
    for i in l:
        if i.isalpha():
            sol.append(i[:n])
        else:
            continue
        
    return sol

def trunk_compre(l: list, n: int) -> list:
    """Shortens strings in the list to length n"""
    return [i[:n] for i in l if i.isalpha()]

if __name__ == "__main__":
    l = ["Alle","Dokumente","dieser","Dokumentensammlung",":"]
    print(trunk(l, 6))
    print(trunk_compre(l, 6))