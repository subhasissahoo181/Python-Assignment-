class Person:
    country = "India"

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is{self.salary}")

    def takeBreath(self):
        print("I am an Employee so i am luckily breathing...")

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"No salary to programers")

p = Person()
e = Employee()
pr = Programmer()
p.takeBreath()
e.takeBreath()
pr.takeBreath()
# print(p.company())
print(e.company)
print(pr.company)