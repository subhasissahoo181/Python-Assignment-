# Write a program to accept marks of  6 students and display then in a sorted manner.


m1 = int(input("Enter marks  1: "))
m2 = int(input("Enter  marks  2: "))
m3 = int(input("Enter  marks  3: "))
m4 = int(input("Enter  marks  4: "))
m5 = int(input("Enter  marks  5: "))
m6 = int(input("Enter  marks  6: "))


myList = [m1, m2, m3, m4, m5, m6]
myList.sort()
print(myList)