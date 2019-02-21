''' 
Khadeja Khalid 
CIS 41A   Spring 2018 
Unit C take-home assignment
'''
import re

#Part 1
'''
1. a$
2. a{2,4}
3. [ab]
4. [^ab]
5. abc
6. .
7. [.]
8. \w
'''
    
#Part2
#First Script
quote = "Believe you can and you're halfway there." 
print(quote)

location = quote.find("a")

while location != -1:
    print(location)
    location = quote.find("a", location + 1)
    
'''
Execution results: 
Believe you can and you're halfway there.
13
16
28
32
'''
    
#Second Script
valid = False
while not valid:
    userInput1 = int(input("Please enter a number between 10-20: "))
    if 10 <= userInput1 <= 20:
        valid = True
    else:
        print("Invalid Input.")
print("Input:", userInput1)

'''
Execution results: 
Please enter a number between 10-20: 6
Invalid Input.
Please enter a number between 10-20: 26
Invalid Input.
Please enter a number between 10-20: 16
Input: 16
'''

#Third Script 
userInput2 = ""

while userInput2 != "Q":
    userInput2 = input("Please input: ")
    if re.search("^\d", userInput2):
        print("Starts with #:", userInput2)
        
''' 
Execution results: 
Please input: 29 palms
Starts with #: 29 palms
Please input: b52s
Please input: 42
Starts with #: 42
Please input: Q
''' 