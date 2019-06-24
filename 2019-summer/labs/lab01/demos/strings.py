#!/usr/bin/env python3

s1 = 'hello ppl'
s2 = 'aloha'

print(s1, id(s1))
s1 = 'h' + s1[1:]
print(s1, id(s1))
s1 = '' + s1[1:]
print(s1, id(s1))

# +
print('a' + 'b' + 'c')
# * 
print('x' * 10)
# []
print(s2[3])
# [:] - x:y:p -> for (i = x; i < y; i += p)
print(s2[:3])
print(s1[::2])
# (not) in
print('h' in s2)

sx = 'abc'
sy = 'aabc'
print(id(sx), id(sy))

s3 = 'hei'
s3[2] = 'y'
print(s3)

# Stringurile sunt similare cu listele.
# Pot fi indexate la fel:
s = "abcd"
print(s[1])

# Putem selecta un substring la fel cum selectam o parte a unei subliste:
s = "banana"
ss = s[2:]
print(ss)

# Pentru a selecta ultime 3 caractere procedam in felul urmator:
w = s[-3:]
print(w)

# Pentru a selecta un interval:
c = s[2:4]
print(c)

# Operatii comune cu stringuri:
# a) concatenarea:
s1 = "ana"
s2 = "maria"
s3 = "ana" + "-" + "maria"
print(s3)

# de obicei, cand aveti erori in printarea unei concatenari de stringuri, este
# pentru ca nu toate elementele concatenate au tipul string
# exemplu:
x = 100
#print("Variabila x are valoarea " + x) # gresit
print("Vairabila x are valoarea " + str(x))

# b) repetarea unui string
# putem inmulti un numar k cu un string s pentru a obtine stringul format prin
# concatenarea lui s cu el insusi de k ori
s = "na"
k = 10
string = k * s + " batman"
print(string)

# c) cautarea unui substring intr-un string
s = "Din cauza rupturii de ligament, Andrei nu va mai putea juca fotbal pana anul viitor"
print("ligament" in s)
print("liga" in s)
print("ligma" in s)

# daca dorim sa aflam si pozitie primei aparitii a substringului in string,
# folosim metoda find()
print(s.find("cauza"))

# putem si sa aflam numarul de aparitii ale subsitringului folosind metoda count()
print(s.count("an"))

# d) inlocuirea unui substring cu altul
s = "Ana are mere"
s = s.replace("mere", "portocale") # inlocuirea nu se face in-place
print(s)

# e) eliminarea caracterelor whitespace de la inceputul si finalul stringului
s = "         https://www.google.com       "
print(s.strip() + " este url-ul fara whitespace-uri aditionale)")
print()
s = "a" + s + "d"
print(s.strip() + " contine caracterele whitespace deoarce nu sunt la inceput sau sfarsit")
print()

# pentru a considera alt caracter drept whitespace il dam ca argument metodei strip()
s = "0000000000https://ww.google.com000000000000"
print(s.strip("0"))
