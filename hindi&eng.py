# Write a program to create a dictionary of Hindi words with values as their english translation Provide user with an option to look it up!

myDict = {
    "Pankha":"Fan",
    "Dabba":"Box",
    "Vastu":"Item"
}
print("Options are ", myDict.keys())
a = input("Enter the Hindi Word\n")
# print("The meaning of your word is:", myDict[a])

# Below line will not throw an error if the key is not present in the dictonary.
print("The meaning of your word is:",myDict.get(a))