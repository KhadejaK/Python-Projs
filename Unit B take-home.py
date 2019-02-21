''' 
Khadeja Khalid 
CIS 41A   Spring 2018 
Unit B take-home assignment

The Vegetable Garden can have Vegetables, and there is no maximum height.
The Low Garden can have Flowers, and there is a maximum height of 3.
The High Garden can have Flowers, and there is a maximum height of 6.
'''

plantName = str(input("Please enter the plant name: "))
plantType = str(input("Please enter the plant type: "))
maxHeight = int(input("Please enter the maximum height of the plant: "))
    
if (plantType == "Vegitable"):
    print ("A(n)", plantName, "can be planted in the Vegitable Garden")
elif (plantType == "Flower"):
    if (maxHeight <= 6 and maxHeight <= 3):
        print ("A(n)", plantName, "can be planted in the Low Garden or the High Garden")
    elif (maxHeight <= 6 and maxHeight > 3):
        print ("A(n)", plantName, "can be planted in the High Garden")
    elif (maxHeight < 0 and maxHeight <= 3):
        print ("A(n)", plantName, "can be planted in the Low Garden")
    else:
        print ("Height is too high")
else:
    print ("A(n)", plantType, "is not a valid type")
    
'''
Results:
Please enter the plant name: Bonsai
Please enter the plant type: Tree
Please enter the maximum height of the plant: 2
A(n) Tree is not a valid type

Please enter the plant name: Carrots
Please enter the plant type: Vegitable
Please enter the maximum height of the plant: 1
A(n) Carrots can be planted in the Vegitable Garden

Please enter the plant name: Corn
Please enter the plant type: Vegitable
Please enter the maximum height of the plant: 8
A(n) Corn can be planted in the Vegitable Garden

Please enter the plant name: Lily
Please enter the plant type: Flower
Please enter the maximum height of the plant: 3
A(n) Lily can be planted in the Low Garden or the High Garden

Please enter the plant name: Rose
Please enter the plant type: Flower
Please enter the maximum height of the plant: 5
A(n) Rose can be planted in the High Garden

Please enter the plant name: Sunflower
Please enter the plant type: Flower
Please enter the maximum height of the plant: 8
Height is too high
'''
        
    