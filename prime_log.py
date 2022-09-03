# Write a program to prime a log file and find out where it contains 'python'.

with open("ch-9/log.txt") as f:
    content = f.read()

if 'python' in content.lower():
    print("Yes python is present.")
else:
    print("No python is not present.") 