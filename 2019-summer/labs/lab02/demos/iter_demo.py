# -*- coding: utf-8 -*-

"""
Author: Iridon Stefan
Curs py@ccna
"""

#Iterables: list, tuple, string, set, dict

mylist = [1, 2, 3]
for i in mylist:
    print(i, end=" ")
print()
#in "spate" se fac urmatorii pasi:
#se obtine un obiect de tip iterator din mylist
myiter = iter(mylist)

#se parcurge iteratorul cu next si se printeaza elementele
print(next(myiter), end=" ")
print(next(myiter), end=" ")
print(next(myiter), end=" ")
