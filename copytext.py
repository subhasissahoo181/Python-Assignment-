# Write a program to make a copy of text file  "this.txt"

from email import contentmanager


with open("ch-9/this.txt") as f:
    content = f.read()

with open("ch-9/copy.txt",'w') as f:
    f.write(content)