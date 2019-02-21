'''
Khadeja Khalid
CIS 41A Spring 2018
Unit A take-home
'''

import math

#... Part 1 ...
print("Part 1")
a = 3 ** 2.5
print("a:", a)
b = 2
b += 3
print("b:", b)
c = 12
c /= 4
print("c:", c)
d = 5%3
print("d:", d)
print()

#... Part 2 ...
print("Part 2")
print("a:", abs(5-7))
print("b:", round(3.14159, 4))
c = 186282/1000
print("c:", round(c)*1000) 
#round(1000, -4)
print("d:", min(6, -9, -3, 0))
print()

#... Part 3 ...
print("Part 3")
num = float(input("Please input a number: "))
print("Square Root:", round(math.sqrt(num), 2))
print("Natural Log:", round(math.log(num), 2))
print()

#... Part 4 ...
print("Part 4")
firstName = str(input("Please input your first name: "))
lastNamee = str(input("Please input your last name: "))
firstNameUpper = firstName.upper()
lastNameeUpper = lastNamee.upper()
print("Uppercase:", firstNameUpper, lastNameeUpper)
print("First Name Length:", len(firstName))
print("3rd Character of Last Name:", lastNamee[2])
print('{:^20}'.format(firstName))
print()

'''
Results
Part 1
a: 15.588457268119896
b: 5
c: 3.0
d: 2

Part 2
a: 2
b: 3.1416
c: 186000
d: -9

Part 3
Please input a number: 7.6
Square Root: 2.76
Natural Log: 0.88

Part 4
Please input your first name: George
Please input your last name: Washington
Uppercase: GEORGE WASHINGTON
First Name Length: 6
3rd Character of Last Name: s
       George       
'''