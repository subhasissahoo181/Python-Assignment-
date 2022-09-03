# Create a class with a class attribute a;
#Create an object from it and set a directly using object a=0 Does this change the class attribute?

from random import sample


class Sample:
    a = 'subhasis' # class attribute

obj = Sample()
obj.a = "Chandan" # instance attribute
Sample.a ="Demo"

print(Sample.a)
print(obj.a)