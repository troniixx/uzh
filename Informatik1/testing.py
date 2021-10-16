list_me = []

f = open("my_grades.txt")

lines = f.readlines()
for line in lines:
    x = line.find(":")
    list_me.append(line[x+1:])
    print(line)

print(list)
