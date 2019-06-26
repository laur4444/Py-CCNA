# -*- coding: utf-8 -*-

"""
Author: Iridon Stefan
Curs py@ccna
"""

#generator function
def generator(low, high):
    while low < high:
        yield low
        low += 1

res = generator(1, 10)

#cu next obtinem cate un element din generator
print(next(res))
print(next(res))
print(next(res))


#observatie: avantajul generatoarelor este modul in care acestea "returneaza" numerele => lazy
#prin generare "lenesa" (la cerere) se obtine o utilizare mai eficienta a memoriei
#nu se mai umple memoria cu toate elementele dintre low si high deoarece se genereaza cate un numar pe rand


lst = list(range(0, 10))
print(sum(lst))
print(sum(generator(0, 10))) #mai eficient din punct de vedere al memoriei folosite

#observatie: generatorul este tot un iterator => putem itera prin el cu for

for i in generator(0, 10):
    print(i, end=" ")

print()

#generator expression
expr = (x ** 2 for x in range(10) if x % 2 == 0)
print(next(expr), end=" ")
print(next(expr), end=" ")
print(next(expr), end=" ")
for i in expr:
    print(i, end=" ")

print()

#observatie: un generator expression se creaza asemanator unui list comprehension
#singura diferenta consta in tipul de paranteze folosit
#la list comprehension se folosesc paranteze drepte
#la generator expression se folosesc paranteze rotunde
