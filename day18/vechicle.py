'''Task: 
Create a parent class Vehicle with:

An attribute brand.

A method describe() that returns: "This is a vehicle."

Create a child class Car that inherits from Vehicle and:

Adds an attribute model.

Overrides the describe() method to return: "This is a [brand] [model]."

Test it:
Create an object of Car and call its describe() method.'''

class Vehicle ():
    brand = ""
    def __init__(self,name):
        self.brand = name
    def describe(self):
        return "This is a vehicle.."
class Car(Vehicle):
    model =""
    def __init__(self, name, model):
        super().__init__(name)
        self.model =model
    
    def describe(self):
        return f"This is a {self.brand} {self.model}."
    
car = Car("BMW","x7")
print(car.describe()) 