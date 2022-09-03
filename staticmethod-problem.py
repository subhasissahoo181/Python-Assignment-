#Add a static method in problem 2 to greet the user with hello.

class Calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The value of {self.number} square is {self.number **2}")
    def squareRoot(self):
        print(f"The value of {self.number} square is {self.number **0.5}")
    def cube(self):
        print(f"The value of {self.number} square is {self.number **3}")

    @staticmethod
    def greet():
        print("### hello User ###")

a = Calculator(3)
a.greet()
a.square()
a.squareRoot()
a.cube()
