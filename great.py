# Write a program to great all the person names stored in a list L1 and which starts with S 
#  l1 = ["subhasis", "subham","sachine","Sachin","Rahul"]

l1 = ["subhasis", "subham","sachine","Sachin","Rahul"]

for name in l1:
    if name.startswith("s"):
        print("Hello  " + name)