# Class Attributes.

from cgi import print_arguments


class Employee:
    company = "Google"

subhasis = Employee()
chandan = Employee()
print(subhasis.company)
print(chandan.company)

Employee.company = "YouTube"
print(subhasis.company)
print(chandan.company)

subhasis.salary = 500
chandan.salary = 600

print(subhasis.salary)
print(chandan.salary)