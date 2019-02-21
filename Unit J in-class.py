# 
# Khadeja Khalid
# CIS 41A Spring 2018
# In-class Assignment J
#
import math

class Circle():
    def __init__(self, radius):
        self.radius = radius
    
    def getArea(self):
        return math.pi * (self.radius**2)
    
class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height
    
    def getVolume(self):
        return super().getArea() * self.height

s1 = Circle(4)
print("Circle area is:", round(s1.getArea(), 2))

s2 = Cylinder(2,5)
print("Cylinder volume is:", round(s2.getVolume(), 2))