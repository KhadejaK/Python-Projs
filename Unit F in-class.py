# 
# Khadeja Khalid
# CIS 41A Spring 2018
# In-class assignment F
#

#Part 1
def byVal(arg):
    print("Arg ID Before: ", id(arg))
    arg = arg + 7
    print("Arg ID After: ", id(arg))
    print()
    
def byRef(agh= []):
    print("Agh ID Before: ", id(agh))
    print("Agh last ID Before: ", id(agh[-1]))
    agh[-1] = agh[-1] + 7
    print("Agh ID After: ", id(agh))
    print("Agh last ID After: ", id(agh[-1]))
    print()
    
#Part 2
def buildBell(rows):
    table = []
    initial = 1
    for i in range(rows):
        list1 = []
        list1.append(initial)
        for j in range(1,i+1):
            list1.append(list1[j-1] + table[i-1][j-1])
        table.append(list1)
        initial = list1[-1]
    printBell(table)
    
def printBell(table):
    for x in range(len(table)):
        for y in range(len(table[x])):
            print (str(table[x][y]).rjust(5, " "), end=" ")
        print()
    
def main():
    myInt = 3
    myList = [0, 1, 2]
    print("OG myInt ID:", id(myInt))
    print("OG myList ID:", id(myList))
    print("OG myList last ID:", id(myList[-1]))   
    print()
    byVal(myInt)
    byRef(myList)
    print("myInt ID:", id(myInt))
    print("myList ID:", id(myList))
    print("myList last ID:", id(myList[-1]))
    print("myInt is now:", myInt)
    print("myList is now:", myList)
    print()
    
    buildBell(8)
    
main()
    