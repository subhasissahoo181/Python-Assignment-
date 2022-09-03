# 01 Write a program to find greatest of four numbers entered by the user.

a =  int(input("Enter number 1: "))
b =  int(input("Enter number 2: "))
c =  int(input("Enter number 3: "))
d =  int(input("Enter number 4: "))

# if(a>b & c>d & b>c):{
#     print(str(a) + " is greatest.")
# }
# elif(b>c & c>d):{
#     print(str(b) + " is greatest.")
# }
# elif(c>d):{
#     print(str(c) + " is greatest.")
# }
# else:{
#     print(str(d) + " is greatest.")
# }

if(a>b):
    f1=a 
else:
    f1=b
if(c>d):
    f2=c 
else:
    f2=d 
if(f1>f2):
    print(str(f1) + " is greater")
else:
    print(str(f2) + " is greater")