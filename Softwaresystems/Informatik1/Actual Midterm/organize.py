def organise(records):
    # { user: {shop -> {day -> counter}}}
    res = {}
    for person, shop, day in records:
        if person and shop and (0 < day < 8):
            if person not in res:
                res[person] = {}
            if shop not in res[person]:
                res[person][shop] = {}
            if day not in res[person][shop]:
                res[person][shop][day] = 0
            res[person][shop][day] += 1
    return res

assert(organise([]) == {})
assert(organise([('Tom', '', 5), ('Tom', 'Aldi', 4)]) == {'Tom': {'Aldi': {4: 1}}})
assert(organise([('Tom', 'Aldi', 5), ('Tom', 'Aldi', 5)]) == {'Tom': {'Aldi': {5: 2}}})
assert(organise([('Tom', 'Aldi', 1), ('Tom', 'Migros', 4), ('Jack', 'Aldi', 5)]) == {'Jack': {'Aldi': {5: 1}}, 'Tom': {'Aldi': {1: 1}, 'Migros': {4: 1}}})