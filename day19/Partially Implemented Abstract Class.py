'''Partially Implemented Abstract Class
Instructions:

Create an abstract class named Employee:

Abstract method: calculate_salary().

Concrete method: display_role() (prints role).

Create concrete classes:

FullTimeEmployee with a calculate_salary() method.

PartTimeEmployee with a calculate_salary() method.

Instantiate both and test both methods.'''

from abc import ABC ,abstractmethod

class Employee():
    @abstractmethod
    def calculate_salary(self):
        pass
    def display_role(self,role):
        self.role=role
        print(self.role)


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("20000")

class PartTimeEmployee(Employee):
    def calculate_salary(self) :
        print("10000")


F =FullTimeEmployee()
P =PartTimeEmployee()
F.display_role("Full Time Employee")
F.calculate_salary()
P.display_role("Part Time Employee")
P.calculate_salary()
