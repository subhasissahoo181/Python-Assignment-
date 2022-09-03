# Write a python program using function to convert Celsius to Fahrenhite.

def fahrenhite(cel):
    return (cel * (9/5)) + 32

c = int(input('Enter the celsius: '))
f = fahrenhite(c)
print('The fahrenhite: '+str(f))