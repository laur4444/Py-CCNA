#!/usr/bin/env python3

# In general, un dictionar este o multime de asocieri de tipul: cheie -> valoare

# Conceptual, acestea pot fi privite ca o extindere a listelor
culori = ["rosu", "albastru", "galben", "verde"]

# In timp ce elementele unei liste pot fi indexate prin pozitia lor
print(culori[1])
print(culori[2])

# Elementele unui dictionar pot fi indexate prin intermediul cheilor, care 
# pot fi:

# - intregi
numere = {2: "doi", 9: "noua", 13: "treisprezece"}
print(numere[2])

# - siruri de caractere
populatie = {"Romania": 19640000, "Anglia": 54790000}
print(populatie["Romania"])

# - tupluri
anagrame = {("ana", "naa"): True, ("abc", "abb"): False}
print(anagrame[("abc", "abb")])

# In general, cheile trebuie sa fie tipuri imutabile, deci spre exemplu nu vom
# putea avea liste drept chei

# Nu exista o restrictie asupra tipurilor pe care le pot avea valorile


# De asemenea, putem crea un dictionar initial vid, dupa care sa adaugam
# elemente secvential:
culori = {}
culori["alb"]   = 0xFFFFFF
culori["negru"] = 0x000000
culori["rosu"]  = 0xFF0000
print(hex(culori["rosu"]))

# Anterior, am folosit functia hex() pentru a afisa valoarea hexadecimala
# a valorii corespunzatoare culorii "rosu" din dictionar

# Daca nu o foloseam, era afisata valoarea corespunzatoare in sistemul decimal
print(culori["rosu"])


cuvinte = {"a": "animal", "b": "banana", "c": "castravete"}
print(cuvinte)

# Daca vrem sa modificam valoarea pentru o anumita cheie dintr-un dictionar,
# procedam in felul urmator:
cuvinte["b"] = "baioneta"
print(cuvinte)

# Observam astfel ca pentru o cheie nu putem avea mai multe valori
# Putem totusi, sa ocolim aceasta limitare, creand un dictionar pentru care
# valorile sunt liste de elemente:

cuvinte = {"a": ["animal"], "b": ["banana", "baioneta"], "c": "castravete"}
cuvinte["a"].append("aspartan")
print(cuvinte)
