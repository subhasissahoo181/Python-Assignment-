
class Employee:
    company = "Visa"
    eCode = 120

class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level +1

class Programmer(Employee, Freelancer):
    name = "Subhasis"

p = Programmer()
print(p.level)
print(p.company)