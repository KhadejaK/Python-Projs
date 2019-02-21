''' 
Khadeja Khalid 
CIS 41A   Spring 2018 
Unit I take-home assignment
'''
class BritCoins(object):
    __coinValues = {"pound":240, "shilling":12, "penny":1} #value of each type of coin in penny
    
    def __init__(self, **kwargs):
        self.totalPennies = 0
        for coinType, value in kwargs.items():
            self.totalPennies += value*BritCoins.__coinValues[coinType]     
        
    def __add__ (self, other):
        total = self.totalPennies + other.totalPennies
        newBritCoin = BritCoins(**{'penny':total})
        return newBritCoin        
        
    def __sub__ (self, other):
        total = self.totalPennies - other.totalPennies
        newBritCoin = BritCoins(**{'penny':total})
        return newBritCoin
        
    def __str__ (self):
        pounds = self.totalPennies//240
        shillings = (self.totalPennies - (pounds*240))//12
        pennies = self.totalPennies - (pounds*240) - (shillings*12)
        return str(pounds)+ " pounds "+ str(shillings)+ " shillings "+ str(pennies)+ " pennies "
                   
c1 = BritCoins(**{'pound':4, 'shilling':24, 'penny':3})
c2 = BritCoins(**{'pound':3, 'shilling':4, 'penny':5})
c3 = c1 + c2 
c4 = c1 - c2

print(c1)
print(c2)
print(c3)
print(c4)

''' 
Execution results:

5 pounds 4 shillings 3 pennies 
3 pounds 4 shillings 5 pennies 
8 pounds 8 shillings 8 pennies 
1 pounds 19 shillings 10 pennies 
''' 