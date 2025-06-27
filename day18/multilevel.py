'''Task: Multilevel Inheritance
Create a class Number:

Attribute: value.

Create a class SquareNumber that inherits from Number:

Method: square() → returns value * value.

Create a class CubeNumber that inherits from SquareNumber:

Method: cube() → returns value * value * value.

Test:

Number(2) → value = 2

SquareNumber(3).square() → 9

CubeNumber(3).cube() → 2'''
class Number():
    value =""
    def __init__(self,name):
        self.value = name
        
class squarenumber(Number):
        def square(self):
            return self.value * self.value

class cubenumber(squarenumber):
     def cube(self):
            return self.value * self.value * self.value
     
num= Number(2)
print(num.value) 
squ =squarenumber(3)
print(squ.square())
cub = cubenumber(4)
print(cub.cube())


        