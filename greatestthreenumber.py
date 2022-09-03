# Write a program using function to find greatest of three numbers.


# from codecs import escape_encode

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
def function(num1, num2, num3):
    if( num1 > num2):
        if(num1 > num3):
            # return num1
            print(num1,'is greater.')
        else:
            # return num3
            print(num3,'is greater.')
    else:
        if(num2 > num3):
            # return num2
            print(num2,'is greater.')
        else:
            # return num3
            print(num3,'is greater.')

f = function(num1,num2,num3)
print(f)