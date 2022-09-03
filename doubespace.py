# Write a program to detected double space in a String .

import string


string = "This is a String width double  spaces." 

doubleSpace = string.find("  ")
print(doubleSpace)