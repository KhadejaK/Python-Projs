# 
# Khadeja Khalid
# CIS 41A Spring 2018
# In-class assignment G
#

#Part 1
file = open("ZenOfPython.txt", "w+")
file.write("Beautiful is better than ugly."+'\n'+"Explicit is better than implicit."+'\n')
file.close()
file = open("ZenOfPython.txt", "a")
file.write("Readability counts."+'\n'+"If the implementation is hard to explain, it's a bad idea.")
file.close()
file = open("ZenOfPython.txt", "r")

line = file.readline()
while line != "":
    print(line.rstrip('\n'))
    line = file.readline()
print()
file.close()

#Part 2
class1 = {"Li", "Audry", "Jia", "Migel", "Tanya"}
class2 = {"Sasha", "Migel", "Tanya", "Hiroto", "Audry"}

class2.add("John")

print("Students in both classes:", sorted(class1 & class2))
print("All students:", sorted(class1 | class2))

if "Sasha" in class1:
    print("Sasha is in class1")
else:
    print("Sasha is not in class1")