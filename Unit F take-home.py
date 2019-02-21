''' 
Khadeja Khalid 
CIS 41A   Spring 2018 
Unit F take-home assignment
'''
#Script 1
def main1():
    listSwap()
    
def listSwap():
    list1 = [4, 2, 3]
    list2 = [1, 5, 6]
    list1[0], list2[0] = list2[0], list1[0]
    print(list1)
    print(list2)
    print()

main1()
'''
Execution Results:
[1, 2, 3]
[4, 5, 6]
'''

#Script 2
def main2():
    printGroupMembers("Group A", "Li", "Audry", "Jia") 
    groupB = ["Group B", "Sasha", "Migel", "Tanya", "Hiroto"] 
    printGroupMembers(*groupB)
    
def printGroupMembers(groupName, *names):
    print("Members of", groupName)
    print("\n".join(names))
    print()
    
main2()
'''
Execution Results:
Members of Group A
Li
Audry
Jia

Members of Group B
Sasha
Migel
Tanya
Hiroto
'''
#Script 3
import math
def main3():
    interestCompound()
    
def interestCompound():
    balance = 1000
    years = [1, 2, 3, 4, 5, 6]
    
    interest = [round(balance*math.e**(.05*e), 2) for e in years]
    
    print(interest)
    
main3()
'''
Execution Results:
[1051.27, 1105.17, 1161.83, 1221.4, 1284.03, 1349.86]
'''

