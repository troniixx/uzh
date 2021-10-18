list_me = []
s = ""
list_us = []

f = open("my_grades.txt")

#get all values after : from txt file
lines = f.readlines()
for line in lines:
    x = line.find(":")
    list_me.append(line[x+1:])
    #print(line)

#get rid of newlines
for e in list_me:
    list_us.append(e.strip())

#removing emtpy strings
while "" in list_us:
    list_us.remove("")

new_list = []
for e in list_us:
    if e in ("1.0", "1.25","1.5", "1.75", "2.0", "2.25", "2.5", "2.75", "3.0", "3.25", "3.5", "3.75", 
    "4.0", "4.25", "4.5", "4.75", "5.0", "5.25", "5.5", "5.75", "6.0"):
        new_list.append(e)
list_us = new_list

#convert elements to int
test_list = [float(i) for i in list_us]
list_us = test_list

avg = sum(list_us)/len(list_us)

print(list_us)
print("sum = ", sum(list_us))
print("avg = ", avg)
