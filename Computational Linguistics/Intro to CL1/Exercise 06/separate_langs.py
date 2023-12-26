
# read in the file
# then split the file into two lists: source_lang and target_lang
PATH = "/Users/merterol/uzh/Computational Linguistics/Intro to CL1/Exercise 06/ro_en.txt"

source_lang = []
target_lang = []

with open(PATH, 'r', encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines:
        # skip irrelevant or wrongly formatted (should not be the case) lines
        if ">" not in line:
            continue

        if line.startswith('(src)'):
            # remove the start of the line until the > symbol
            line = line.split('>')[1]
            source_lang.append(line.strip('\n'))
        elif line.startswith('(trg)'):
            # remove the start of the line until the > symbol
            line = line.split('>')[1]
            target_lang.append(line.strip('\n'))


source_lang_str = ' '.join(source_lang)
target_lang_str = ' '.join(target_lang)

# write both strings into separate files
with open('source.txt', 'w', encoding="utf-8") as f:
    f.write(source_lang_str)

with open('target.txt', 'w', encoding="utf-8") as f:
    f.write(target_lang_str)