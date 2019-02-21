# 
# Khadeja Khalid
# CIS 41A Spring 2018
# In-class assignment E
#

#Part 1 
import random

def welcome():
    print("Welcome to the Dice Rolling Game")
    
def rollDie(sides):
    roll = random.randint(1, sides)
    return roll
    
def playGame(runs):
    length = runs
    moneyTotal = 0
    moneyMax = []
    moneyCurrent = 0    
    welcome()
    while runs > 0 :
        rolls = rollDie(6) 
        while 3 < rolls <= 6 :
            moneyCurrent = moneyCurrent + rolls
            rolls = rollDie(6)  
        else :
            runs = runs-1     
            moneyMax.append(moneyCurrent)
            moneyTotal += moneyCurrent
            moneyCurrent = 0    
    print("Max: $", max(moneyMax))
    print("Average: $", round(moneyTotal/length, 2))    

#Part 2
import copy
'''
1. Create a list called list1 that is populated with the elements 2,4,6.
2. Copy list1 to list2 so that list2 is an alias of list1 (shallow copy).
3. Copy list1 to list3 so that list3 is a new list (deep copy).
4. Append the value 8 to list1.
5. After the first element of list2, insert the value 3.
6. Remove (pop) the first element from list3.
7. Print all three lists, along with a text description that identifies the list being printed.
Note that you don't have to loop through the list to print it, simply print the entire list. 
Do the results match what you expected?
'''
def funWithLists():
    list1 = [2, 4, 6]
    list2 = copy.copy(list1)
    list3 = copy.deepcopy(list1)
    list1.append(8)
    list2.insert(1, 3)
    list3.pop(0)
    print("List1: ", list1)
    print("List2: ", list2)
    print("List3: ", list3)
    
def main():
    runs = int(input("Please enter # of runs: "))
    playGame(runs)
    funWithLists()

    
main()
'''
Results:
Please enter # of runs: 10000
Welcome to the Dice Rolling Game
Max: $ 94
Average: $ 8.96
List1:  [2, 4, 6, 8]
List2:  [3, 2, 4, 6]
List3:  [4, 6]

'''
    
    
    