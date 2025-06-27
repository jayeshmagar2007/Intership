'''Task: Getters and Setters
Instructions:

Create a class Person.

Add a private attribute __age.

Create:

A method set_age(value) that validates if the age is a positive number.

A method get_age() to return the age.

Try setting both valid and invalid ages.'''

class Person():
    def __init__(self,age):
        self.__age=age
    def set_age(self,val):
        if val > 0:
            self.__age = val
        else: 
            print("Invalid age ")

    def get_age(self):
        return self.__age
    
p=Person(23)
p.set_age(-2)
p.set_age(33)
print(p.get_age())
        