print("Question 1")

genotypes = [1, 4, 2, 1, 3, 4, 3, 4, 1, 4, 3, 2, 4, 4, 2]

cnt = 0

for i in genotypes:
    if i < 4: cnt += 1
    
print(cnt)
print(cnt / len(genotypes))

print("=====================================")
print("Question 2")

codons = ['TCG', 'ATG', 'ATT', 'TCT', 'GAC', 'ATG', 'GCG',
'TCA', 'ATG', 'GTA', 'CTC', 'GCG', 'GAG']

sol = {}

for idx, c in enumerate(codons):
    if c not in sol:
        sol[c] = []
        sol[c].append(idx)
    else:
        sol[c].append(idx)
        
print(sol)

print("=====================================")
print("Question 3")

def meltingTemperature(seq):
    cnt_a = 0
    cnt_c = 0
    cnt_t = 0
    cnt_g = 0
    
    for char in seq:
        match char:
            case "A":
                cnt_a += 1
            case "C":
                cnt_c += 1
            case "T":
                cnt_t += 1
            case "G":
                cnt_g += 1
                
    return 4 * (cnt_g + cnt_c) + 2 * (cnt_a + cnt_t)


print(meltingTemperature('TCAGCTAGCTCGTAGCTACAGGC'))
print(meltingTemperature('TGAAGTGTGAATAGTACTCACGAG'))

print("=====================================")
print("Question 4")


print("=====================================")
print("Question 5")

encoded = 'rtrjsyx ufxx, zsstynhji, zsynq ymjd fwj ltsj.'
key = 'fghijklmnopqrstuvwxyzabcde'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Create a mapping dictionary
decode_dict = {k: a for k, a in zip(key, alphabet)}

s = ""

for char in encoded:
    if char in decode_dict:
        s += decode_dict[char]
    else:
        s += char

print(s)