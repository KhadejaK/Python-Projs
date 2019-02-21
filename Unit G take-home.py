''' 
Khadeja Khalid 
CIS 41A   Spring 2018 
Unit G take-home assignment
'''
#Script 1
def main1():
    states()
    
def states():
    file = open("states.txt", "r")
    topPop = 0
    
    line = file.readline() 
    while line != "" :   
        space = line.rsplit(" ")
        state = space[0]
        region = space[1]
        population = int(space[2])
        if region == "Midwest":
            if population > topPop:
                topPop = population
                topPopState = state
        line = file.readline()
        
    print("Highest population state in the Midwest is:", topPopState, topPop)
    print()
        
main1()
''' 
Execution results:
Highest population state in the Midwest is: IL 12802000
'''

#Script 
def main2():
    errors()
    
def errors():
    list1 = [1, 2, 3]
    try:
        print(list1[3])
    except:
        print("Error: bad index number.")
        print()
    
main2()
''' 
Execution results:
Error: bad index number.
'''

#Script 3
def main3():
    classSets()
    
def classSets():
    class1 = {"Li", "Audry", "Jia", "Migel", "Tanya"}
    class2 = {"Sasha", "Migel", "Tanya", "Hiroto", "Audry"}
    class3 = {"Migel", "Zhang", "Hiroto", "Anita", "Jia"}
    
    print("Students in all three classes:", sorted(class1 & class2 & class3))
    print("All students:", sorted(class1 | class2 | class3))
    print("Students in class1 but not class2 or class3:", sorted((class1 - (class2 | class3))))
    
main3()
''' 
Execution results:
Students in all three classes: ['Migel']
All students: ['Anita', 'Audry', 'Hiroto', 'Jia', 'Li', 'Migel', 'Sasha', 'Tanya', 'Zhang']
Students in class1 but not class2 or class3: ['Li']
'''
