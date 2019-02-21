''' 
Khadeja Khalid 
CIS 41A   Spring 2018 
Unit H take-home assignment
'''
#Part 1
def main1():
    uspres()
    
def uspres():
    dictionary = {}
    file = open("USPresidents.txt","r")
    line = file.readline() 
    while line != "" :    
        space = line.split()
        if space[0] in dictionary:
            dictionary[space[0]].append(space[1])
        else:
            pres = []
            pres.append(space[1])
            dictionary[space[0]] = pres
        line = file.readline()  
            
    stateMax, presMax = max(dictionary.items(), key = lambda x: len(set(x[1])))
    print("The state with the most presidents is", stateMax, "with", len(presMax), "presidents:")
    for pres in presMax:
        print (pres)    
    
main1()

''' 
Execution results:

The state with the most presidents is VA with 8 presidents:
George_Washington
James_Madison
James_Monroe
John_Tyler
Thomas_Jefferson
William_Henry_Harrison
Woodrow_Wilson
Zachary_Taylor
'''

print()
#Part 2
def main2():
    uspres2()
    
def uspres2():
    presCount = {}
    file = open("USPresidents.txt","r")
    line = file.readline() 
    while line != "" :    
        space = line.split()
        if space[0] in presCount:
            presCount[space[0]] += 1
        else:
            presCount[space[0]] = 1
        line = file.readline()  
        
    topTen = {"CA", "TX", "FL", "NY", "IL", "PA", "OH", "GA", "NC", "MI"}
    
    topBorn = set(topTen & presCount.keys())
    
    print (len(topBorn), "of the", len(topTen), "high population states have had presidents born in them:")
    for elm in sorted(topBorn):
        print (elm, presCount[elm])   
    
main2()

''' 
Execution results:

8 of the 10 high population states have had presidents born in them:
CA 1
GA 1
IL 1
NC 2
NY 5
OH 7
PA 1
TX 2
'''

print()
#Part 3
def main3():
    Message1 = {'temperature':550}
    Message2 = {'temperature':475}
    Message3 = {'temperature':450, 'miscError': 404}
    Message4 = {'CO2level':.18}
    Message5 = {'CO2level':.2, 'miscError':503}  
    overseerSystem(**Message1)
    overseerSystem(**Message2)
    overseerSystem(**Message3)
    overseerSystem(**Message4)
    overseerSystem(**Message5)
    
def overseerSystem(**kwargs):
    if 'temperature' in kwargs:
        if kwargs['temperature'] > 500:
            print("Warning: Temperature is", kwargs['temperature'])
    if 'CO2level' in kwargs:
        if kwargs['CO2level'] > 0.15:
            print("Warning: CO2 level is", kwargs['CO2level'])
    if 'miscError' in kwargs:
        print("miscError #", kwargs['miscError'])
    
main3()
    
''' 
Execution results:

Warning: Temperature is 550
miscError # 404
Warning: CO2 level is 0.18
Warning: CO2 level is 0.2
miscError # 503
'''