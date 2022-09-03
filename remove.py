# Write a python function to remove a given word form a list and setup at the same time.

#------- Strip in python -----------
# f = "   chandan   "
# print(f)

# hear the space before the chandan known as Strip.

def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "  Hello Subhasis  "
n = remove_and_split(this, "Subhasis")
print(n)