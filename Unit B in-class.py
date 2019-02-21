# 
# Khadeja Khalid
# CIS 41A Spring 2018
# Take-home assignment B
#

quote = "Believe you can and you're halfway there." 

print(quote)
print(quote.count("a"))

location = quote.find("a")
print(location)

location = quote.find("a", location + 1)  
print(location)

location = quote.find("a", location +1)
print(location)

location = quote.find("a", location +1)
print(location)
      
location = quote.find("a", location +1)
print(location)

print(quote.isalnum())
print(quote.isalpha())
print(quote.isdigit())
print(quote.islower())
print(quote.isspace())
print(quote.isupper())

'''
Believe you can and you're halfway there.
4
13
16
28
32
-1
False
False
False
False
False
False
'''