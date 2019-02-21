# 
# Khadeja Khalid
# CIS 41A Spring 2018
# In-class Assignment H
#

#Part 1
fruitDessert = {'apple':"sauce", 'peach':"cobbler", 'carrot':"cake", 'strawberry':"sorbet", 'banana':"cream pie"}
fruitDessert['mango'] = "sticky rice"
fruitDessert['strawberry'] = "shortcake"
del fruitDessert['carrot']
print("apple dessert is:", fruitDessert['apple'])
print()
try:
    print("Banana dessert does exist")
    fruitDessert['banana']
except:
    print("Banana dessert does not exist")
print()
try:
    print(fruitDessert['pear'])
except:
    print("Pear dessert does not exist")

print()
for k, v in fruitDessert.items():
    print(k, v)
    
print()
for k, v in sorted(fruitDessert.items()):
    print(k, v)
    
#Part 2
states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California"]
capitols = ["Montgomery", "Juneau", "Phoenix", "Little Rock", "Sacramento"]
dictionary = dict(zip(states, capitols))
print()
for k, v in sorted(dictionary.items()):
    print(k, v)
    

#Part 3
dic = {'California': "Sac.", 'Colorado': "Denver", 'Connecticut': "Hartford"}
dictionary.update(dic)
print()
for k, v in sorted(dictionary.items()):
    print(k, v)
