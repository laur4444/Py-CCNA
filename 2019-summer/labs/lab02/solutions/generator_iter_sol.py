# -*- coding: utf-8 -*-

"""
Author: Iridon Stefan
Curs py@ccna
"""

def divisors(number):
    nr_div = 0
    for i in range(1, number + 1):
        if number % i == 0:
            nr_div += 1
    return nr_div

def divisor_gen_func(number):
    for i in range (1, number + 1):
        yield divisors(i)

no_divs_gen = (divisors(x) for x in range(1, 11))

for i in no_divs_gen:
    print(i, end=" ")
print()
    
for i in divisor_gen_func(10):
    print(i, end=" ")
print()
