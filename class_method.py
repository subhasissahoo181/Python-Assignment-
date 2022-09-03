from pprint import pprint


class Employee:
    company = "Camel"
    salary = 100
    location = "Bhubaneswar"

    # def changeSalary(self, sal):
        # self.salary = sal
        # self.__class__.salary = sal

    @classmethod
    def changeSalary(self, sal):
        self.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)