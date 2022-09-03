# Create a class program for storing information of few programers working at microsoft.

class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the programer is {self.name} and the product is {self.product}")

subhasis = Programmer("subhasiss","skype")
alka =Programmer ("alka","Guiatar")
subhasis.getInfo()
alka.getInfo()