# Write a program which find out wheather a given name is present in a list or not.

# from unicodedata import name


names = ["subhasis" , "chandan" , "das", "sahoo"]
name = input("Enter the name to check\n")

if name in names:
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")