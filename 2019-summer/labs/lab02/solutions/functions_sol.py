# -*- coding: utf-8 -*-

"""
Author: Iridon Stefan
Curs py@ccna
"""

import math

def prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def square(number):
    return number ** 2

def myjoin(mylist, fs = " "):
    return fs.join(mylist)

def prime_squares(n):
    numbers = list(range(2, n))
    primes = list(filter(prime, numbers))
    square_numbers = list(map(square, numbers))
    return square_numbers

print(prime_squares(10))
mylist = ["ana", "are", "mere"]
print(myjoin(mylist))
print(myjoin(mylist, "---"))

