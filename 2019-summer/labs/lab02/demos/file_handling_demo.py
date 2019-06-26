# -*- coding: utf-8 -*-

"""
Author: Iridon Stefan
Curs py@ccna
"""

import os
import sys

#deschidere fisier - built-in functions - open
f1 = open("read_file.txt")
#constructie echivalenta cu: 
#f1 = open("read_file.txt", "rt")
#default rt: r = read; t = text
print(f1.read())

f1 = open("read_file.txt", "rt")
print(f1.read(5)) #citeste 5 caractere incepand cu pozitia cursorului in fisier

f1.seek(0, 0); #deplasarea cursorului la inceputul fisierului (primul argument reprezinta deplasamentul; al doilea reprezinta pozitia)
print(f1.readline()) #citeste linia curenta din fisier

f1.seek(0, 0);
lines = f1.readlines() #se introduc liniile intr-o lista (incepand cu linia curenta)
print(lines)

for line in lines:
	print(line, end = "") #parsare linii din lista

#varianta 2
f1.seek(0, 0);
for line in f1:
	print(line, end = "") #parsare linii direct din fisier
f1.close()

#scriere in fisier
f1 = open("read_file.txt", "a")
f1.write("Adding my line\n")
f1.close()

print("---------------------------------------------------")
#deschidere fisier - os module - fdopen

fd = os.open("read_file.txt", os.O_RDONLY)
f2 = os.fdopen(fd, "r") #fdopen primeste un file descriptor si returneaza un file object
print(f2.read())

os.lseek(fd, 0, 0)
st = os.read(fd, 100) #citeste maxim 100 de caractere din fisier (se obtine byte array) caracterele sunt ascii
string = st.decode("utf-8") #un string contine utf-8
print(st)
print(string)

os.close(fd)

exists = os.path.isfile("nonexistentfile.txt")
if exists == False:
    f2 = os.fdopen(2, "w") #observatie: elegant s-ar folosi sys.stderr.write! acest exemplu are doar scopul de a arata cum se poate interactiona cu fds
    f2.write("error, file does not exist")
    sys.exit(1)
    f2.close()
