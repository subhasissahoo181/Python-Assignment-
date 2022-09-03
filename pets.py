# Create a class pets from a class Animal and further create class Dog from Pets. Add a method bark to class Dog
from turtle import color


class Animals:
    animalType = "Mammal"

class Pets:
    color = "White"

class Dog:
    @staticmethod
    def bark():
        print("Bow Bow!")

d = Dog()
d.bark()