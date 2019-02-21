''' 
Khadeja Khalid 
CIS 41A   Spring 2018 
Unit E take-home assignment
'''
#Script 1
def invoice(unitPrice, quantity, shipping = 10, handling = 5):
    print("Cost (unitPrice x quantity) = ", unitPrice*quantity)
    print("Shipping = ", shipping)
    print("Handling = ", handling)
    print("Total = ", unitPrice*quantity + shipping + handling)
    print()
    
def main1():
    invoice(20, 4, 8)
    invoice(15, 3, handling = 15)
    
main1()
'''
Execution Results:
Cost (unitPrice x quantity) =  80
Shipping =  8
Handling =  5
Total =  93

Cost (unitPrice x quantity) =  45
Shipping =  10
Handling =  15
Total =  70
'''
#Script 2
def uniqueList():
    import random
    num = []
    while len(num) != 10:
        ran = random.randint(1,15)
        if num.count(ran) == 0:
            num.append(ran)
    num.sort()
    print(num)
    print("Sum = ", sum(num))
    print()
    
def main2():
    uniqueList()
    
main2()
'''
Execution Results:
[1, 3, 4, 5, 9, 10, 11, 13, 14, 15]
Sum = 85

[2, 4, 5, 8, 9, 10, 11, 12, 14, 15]
Sum = 90
'''
#Script 3
def rangeList():
    import random
    list1 = []
    for i in range(50, 61, 2):
        list1.append(i)
    random.shuffle(list1)
    print(list1)
    for i in range(0, 6):
        if list1[i] == 50 or list1[i] == 52:
            index = i
            break
    print("Index of first list element less than 53 is: ", index)
    print()
    
def main3():
    rangeList()
    
main3()
'''
Execution Results:
[58, 54, 50, 60, 52, 56]
Index of first list element less than 53 is:  2
'''
#Script 4
def sliceList():
    list2 = []
    for i in range(1,11):
        list2.append(i)
    print('\n'.join(map(str,list2[4:7])))

def main4():
    sliceList()
main4()
'''
Execution Results:
5
6
7
'''
#Script 5 
import random
def rollDie(sides):
    roll = random.randint(1, sides)
    return roll

def diceTest():
    roll1 = []
    roll2 = []    
    rollResults = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0,100000):
        roll1.append(rollDie(6))
        roll2.append(rollDie(6))
        rollResults[roll1[i] + roll2[i]] += 1
    for i in range(0, 13):
        print("Chance of rolling a", i, str(round(rollResults[i]/1000, 2))+"%", end="\n")
        
def main5():
    diceTest()
main5()
''' 
Execution results: 
Chance of rolling a 0 0.0%
Chance of rolling a 1 0.0%
Chance of rolling a 2 2.77%
Chance of rolling a 3 5.58%
Chance of rolling a 4 8.43%
Chance of rolling a 5 11.09%
Chance of rolling a 6 13.83%
Chance of rolling a 7 16.51%
Chance of rolling a 8 14.01%
Chance of rolling a 9 11.14%
Chance of rolling a 10 8.22%
Chance of rolling a 11 5.59%
Chance of rolling a 12 2.85% 
''' 