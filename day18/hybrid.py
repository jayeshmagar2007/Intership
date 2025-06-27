'''Task:
Create a parent class Number.

Create SumNumber and ProductNumber classes that inherit from Number.

Create a final class FinalCalculator that inherits from both.

Call parent methods directly:

SumNumber.sum(self, a, b).

ProductNumber.product(self, a, b).

Test:

FinalCalculator().sum(5, 10) → 15

FinalCalculator().product(3, 4) → 12'''

class Number():
    def __init__(self,a,b):
        self.a =a
        self.b= b
class Subnumber(Number):
    def sum(self,a,b):
        return a+b
class Productnumber(Number):
    def product(self,a,b):
        return a*b
class FinalCalculator(Subnumber, Productnumber):
    def __init__(self):
        pass

print(FinalCalculator().sum(5,10))
print(FinalCalculator().product(3,4))