# Write a program to find out whether a file is identical & matches the content of another file.

# from traceback import print_tb


file1 = "ch-9/copy.txt"
file2 = "ch-9/this.txt"

with open(file1) as f:
    f1 = f.read()

with open(file2) as f:
    f2 = f.read()

if f1 == f2:
    print("Files are identical")
else:
    print("Files are not identical")