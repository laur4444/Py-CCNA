#!/usr/bin/env python3

culori = {}
culori["negru"] = 0x000000
culori["rosu"]  = 0xFF0000
culori["alb"]   = 0xFFFFFF

# Pentru a obtine lista tuturor cheilor din dictionar:
# - in ordinea insertiei:
print(list(culori))

# - in ordine alfabetica:
print(sorted(culori))


# Putem testa apartenta unei chei la un dictionar in felul urmator:
print("negru" in culori)
print("verde" in culori)
print("albastru" not in culori)
print()


# Putem scoate o cheie din dictionar:
print("alb" in culori)

del culori["alb"]

print("after delete:")
print("alb" in culori)


# Un mod aditional de a crea dictionare este folosind constructorul dict()
# asupra unei liste de perechi cheie-valoare:

culori = dict([("negru", 0x000000), ("rosu", 0xFF0000), ("alb", 0xFFFFFF)])
print(culori)
print()

# In unele situatii, un mod mai compact de a defini un dictionar este prin
# list comprehensions; acestea sunt similare notatiei prin care defineam
# elementele unei multimi in notatia matematica
#
# ex: A = {4 * x + 3 | x apartine N}
#
# evident, in python avem limitarea aditionala ca structura de date obtinuta
# sa aiba un numar finit de elemente

# list comprehension pentru o lista cu primii 10 multipli de 3:
mult = {3 * x for x in range(10)}

# list comprehension pentru un dictionar cu lungimea caracterelor unui string
lung = {string : len(string) for string in ("capsuna", "mar", "portocala", "piersica")}
print(lung)
print()

# list comprehension pentru un dictionar ce contine cubul primelor 30 numere naturale:
cube = {x : x**3 for x in range(30)}
print(cube)
print()


# in sfarsit, pentru a itera prin elementele unui dictionar procedam astfel:
for k, v in culori.items():
    print("cheie: " + k + ", valoare: " + hex(v))
