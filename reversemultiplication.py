# Write a program to print multiplication table of N using for loop in reversed order.

num = int(input("Enter the Number: "))

for i in range(1,11):
    
    # print(str(num) + " X " + str(i) + " = " + str(i*num))
    print(f"{num}X{i}={num*i}")