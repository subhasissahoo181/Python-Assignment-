class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name = name 
        self.salary = salary 
        self.subunit = subunit
        print("Employee is Created! ")

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")
    
    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, sir")

    @staticmethod
    def time():
        print("The time is 9pm in the morning")

    
    subhasis = Employee("Subhasis",100,"Coding")
    # Subhasis = Employee() --> This throws an error (missing 3 required positional arguments:)
    subhasis.getDetails()

        