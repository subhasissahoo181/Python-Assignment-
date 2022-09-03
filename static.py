class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, sir")

harry = Employee()
harry.salary = 10000000
harry.getSalary("Thanks!") #Employee.getSalary(harry)
harry.greet() #Employee.greet()