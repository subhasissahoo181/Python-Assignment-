# n! = 1 * 2 * 3 * 4...*n
# n = 5
# product = 1
# for i in range(n):
#     product = product * (i+1)
# print(product)

# from itertools import product


from math import factorial


def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursive(n-1)

f=factorial_recursive(5)
print(f)
# print(factorial_iter(5))