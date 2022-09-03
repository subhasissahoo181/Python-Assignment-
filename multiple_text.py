# A file contains a word "Donkey" multiple times you need to write a program with replaces this word with ###### by updating the same file.


with open("ch-9/multiple_text.txt") as f:
    content = f.read()

content = content.replace("donkey", "#####")

with open("ch-9/multiple_text.txt","w") as f:
    f.write(content)
