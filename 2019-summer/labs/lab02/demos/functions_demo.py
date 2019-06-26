# -*- coding: utf-8 -*-

"""
Author: Iridon Stefan
Curs py@ccna
"""

#functii "void"
def hello():
    print("Hello World!")

def hello_2():
    print("Hello World!")
    return

def hello_3():
    print("Hello World!")
    return None

#observatie:
#   cele 3 functii de mai sus sunt echivalente
#   la o inspectie a bytecode-ului, toate cele 3 functii returneaza "in spate" None
#   5 LOAD_CONST    0 (None)
#   8 RETURN_VALUE
if (hello() == None):
    print("None")
if (hello_2() == None):
    print("None")
if (hello_3() == None):
    print("None")

#functii value-returning
def factorial(a):
    result = 1
    for i in range(a):
        result *= (i + 1)
    return result

print(factorial(3))

#observatie: implementare recursiva
def factorial_rec(a):
    if a == 0 or a == 1:
        return 1
    return a * factorial_rec(a - 1)

print(factorial_rec(3))

#recursivitate pe coada
#avantaj: foloseste mai putina memorie(1 singur stack-frame)
def factorial_tail_rec(a, acc):
    if a == 0 or a == 1:
        return acc
    return factorial_tail_rec(a - 1, a * acc)

print(factorial_tail_rec(3, 1))

#functii multi-value-returning: folosim tupluri
def multi_value():
    return(8, 7)

a = 0
b = 0
print("before: a = " + str(a) + ", b = " + str(b))
a, b = multi_value()
print("after: a = " + str(a) + ", b = " + str(b))

#functii cu argumente default:
#plecam de la implementarea factorialului cu tail recursion
def factorial_default_acc(a, acc = 1):
    if a == 0 or a == 1:
        return acc
    return factorial_default_acc(a - 1, a * acc)

#se observa ca nu mai este necesar sa introducem valoarea lui acc
print(factorial_default_acc(3))

#argumentul default se poate suprascrie:
def sum(a = 1, b = 2):
    print(a + b)

sum()
sum(1, 3)


#functii cu argumente keyword
#avantaj: argumentele se pot da in orice ordine
def quotient(a, b):
    print(a / b)

#rezultatul va fi in continuare a / b
quotient(b = 3, a = 6)

#functii cu numar variabil de argumente
def sum_multiple(*argv):
    result = 0
    for i in argv:
        result += i
    return result

print(sum_multiple(1, 2, 3, 4))

#observatie: alternativa cu liste
def sum_list(l):
    result = 0
    for i in l:
        result += i
    return result

print(sum_list([1, 2, 3, 4]))

#bonus: filter
def even(number):
    if number % 2 == 0:
        return True
    return False

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_evens = filter(even, numbers)
print(list(filtered_evens))

#bonus: map
def add1(number):
    return number + 1

numbers_plus_1 = map(add1, numbers)
print(list(numbers_plus_1))


