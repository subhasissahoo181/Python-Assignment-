# Write a recursive function to calculate the sum of first n natural numbers.

def sum_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

def sum_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n + sum_recursive(n-1)

f=sum_recursive(5)
print(f)