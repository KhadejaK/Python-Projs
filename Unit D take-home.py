''' 
Khadeja Khalid 
CIS 41A   Spring 2018 
Unit D take-home assignment
'''
import re

#First Script
user = int(input("Please enter the number of rows for the multiplication table: "))

for i in range (user):
    for j in range (i+1):
        print(str((i+1)*(j+1)).rjust(4), end="")
    print()

'''
Excecution Result:
Please enter the number of rows for the multiplication table: 12
   1
   2   4
   3   6   9
   4   8  12  16
   5  10  15  20  25
   6  12  18  24  30  36
   7  14  21  28  35  42  49
   8  16  24  32  40  48  56  64
   9  18  27  36  45  54  63  72  81
  10  20  30  40  50  60  70  80  90 100
  11  22  33  44  55  66  77  88  99 110 121
  12  24  36  48  60  72  84  96 108 120 132 144

'''
#Second Script
import random

moneyTotal = []
moneyCurrent = 0

simulations = int(input("Please enter # of simulations: "))
length = simulations

while simulations > 0 :
    roll = random.randint(1, 6)  
    while 3 <= roll <= 6 :
        moneyCurrent = moneyCurrent + roll
        roll = random.randint(1, 6)  
          
    else :
        simulations = simulations-1     
        moneyTotal.append(moneyCurrent)
        moneyCurrent = 0
          
print("Max: $", max(moneyTotal))
print("Average: $", round(sum(moneyTotal)/length, 2))

'''
Excecution Result:
Please enter # of simulations: 10000
Max: $ 105
Average: $ 8.87

'''

#Third Script
quote = "Beautiful is better than ugly - The Zen of Python"

results= re.findall(r"\b\w*?([aeiouAEIOU])", quote)
c = ", ";

print(c.join(results))

'''
Excecution Result:
e, i, e, a, u, e, e, o, o
'''

#Fourth Script
food = "The rabbit, the onion, the garlic, the tomato, some salt, stew and then we have the feast."

recipe = re.sub(r"\b(the|The)\b", "a", food)

print(recipe)

'''
Excecution Result:
a rabbit, a onion, a garlic, a tomato, some salt, stew and then we have a feast.

'''