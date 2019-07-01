
# Pentru a putea folosi functionalitati similare cu cele ale comenzilor din bash,
# putem folosi functiile importate din modulul os:

import os
import os.path as path

# Se poate astfel sa folosim functii echivalente cu cele din bash:
# - pwd
print("Adresa absoluta a directorului curent este:\n" + os.getcwd() + "\n")

# - ls
print("Fisierele si directoarele din directorul curent sunt: ")
for x in os.listdir():
    print(x)

# - mkdir
# de tinut minte ca crearea unui director va genera o exceptie daca acel director deja exista
os.mkdir("director1")
os.mkdir("director2")

# Daca dorim sa cream recursiv o ierarhie de fisiere, varianta de mai jos nu va functiona:
# os.mkdir("facultate/teme/tema1")
# Va trebui sa folosim in schimb functia makedirs():
os.makedirs("facultate/teme/tema1")
os.makedirs("jocuri/warcraft3/")

# - rmdir
# de tinut minte ca stergerea unui director care nu exista va genera o exceptie
os.rmdir("director1")
os.rmdir("director2")
# Functia echivalenta pentru stergerea recursiva a unei ierarhii de fisiere este removedirs()
os.removedirs("facultate/teme/tema1")
os.removedirs("jocuri/warcraft3/")

# - touch
os.mknod("useless_file.txt")
os.mknod("script.sh")

# - chmod
os.chmod("script.sh", 0o777)
# prefixul 0o indica faptul ca numarul este in baza 8
# in bash, numarul primit ca argument de comanda bash, care specifica
# permisiunile, era tot in baza 8, insa nu trebuia sa mentionam acest lucru
# in mod explicit

# - rm
os.remove("useless_file.txt")
os.remove("script.sh")

#TODO: Cautati in documentatia pentru os cum puteti redenumi un fisier
# In plus, mai dispunem de functia rename():

# Pentru a obtine adresa absoluta, cunoscand adresa relativa folosim
# functia abspath()
relative_path = "director"
print("Adresa absoluta a fisierului " + relative_path + " este:")
absolute_path = path.abspath(relative_path)
print(absolute_path)

# Pentru a realiza operatia inversa folosim basename()
print(path.basename(absolute_path))
print()

# Pentru a crea un path din numele unor directoare, putem folosi
# functia join()
print(path.join("facultate", "teme", "tema1", "bin"))
print()
# Avantajul aceste aboradi fata de o constructie de genul:
# print("facultate" + "/" + "teme" + "/" + "tema1" + "/" + "bin")
# este faptul ca join() creaza path-ul in functie de sistemul de operare
# Astfel, pe windows am obtine "facultate\teme\tema1\bin"

#TODO: cautati in documentatia pentru path cum puteti verifica daca un fisier exista deja


# Putem verifica daca un path se refera la un fisier sau la un director astfel:
print(path.isfile("director"))
print(path.isdir("director"))
print()

# Pentru a explicita caracterul ~ in directorul home al utilizatorului curent,
# folosim functia expanduser()
print(path.expanduser("~/Desktop/homework"))