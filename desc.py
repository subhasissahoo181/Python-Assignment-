#

myDict = {
    "fast": "In a Quick Manner",
    "Harry": "A coder",
    "Marks": [1,2,5],
    "anotherdict": {'harry':'Player'},
    1:2
}

# Dictionary Methods 
print(list(myDict.keys())) # Prints the keys of the Dictionary
print(myDict.values()) # print the keys of the Dictionary
print(myDict.items()) #print the (key, value) for all contents of the Dictionary
print(myDict)
updateDict = {
    "Lovish": "friend",
    "Divya": "Friend",
    "Subham":"Friend",
}
myDict.update(updateDict) # Updates 
print(myDict)