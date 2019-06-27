# -*- coding: utf-8 -*-

"""
Author: Iridon Stefan
Curs py@ccna
"""

import os
import sys

#Task01-------------------------------------------------------------------------
input_file = open("lab02_file.txt")
lines = input_file.readlines()
input_file.close()

output_file = open("new_lab02_file.txt", "w")
for line in lines:
    for word in line.split():
        output_file.write(word + "\n")

output_file.close()

#Task02-------------------------------------------------------------------------
new_input_file = open("new_lab02_file.txt")

start = new_input_file.tell()
new_input_file.seek(0, os.SEEK_END)
end = new_input_file.tell()
size = end - start
print(new_input_file.name + " size: " + str(size) + " bytes")

#Task03-------------------------------------------------------------------------
cursor = size / 2
new_input_file.seek(cursor, os.SEEK_SET)
half_data = new_input_file.read()
new_input_file.close()
half_input_file = open("half_lab02_file.txt", "w")
half_input_file.write(half_data)
half_input_file.close()

#Task04-------------------------------------------------------------------------
my_file_name = "gogus_file.txt"
if os.path.isfile(my_file_name) == True:
    sys.stderr.write("Error! File already exists!")
    sys.exit(1)
else:
    my_file = open(my_file_name, "w")
    my_file.write("Gogu\n")
    my_file.write("DeLaGaze\n")
    my_file.write("345CC\n")
    my_file.close()

#Bonus01------------------------------------------------------------------------
input_fd = os.open("new_lab02_file.txt", os.O_RDONLY)
statinfo = os.fstat(input_fd)
print("new_lab02_file.txt size: " +  str(statinfo.st_size) + " bytes")

#Bonus02------------------------------------------------------------------------
output_fd = os.open("bonus_half_lab02_file.txt", os.O_WRONLY|os.O_CREAT)
cursor = int(statinfo.st_size / 2)
os.lseek(input_fd, cursor, os.SEEK_SET)
half_data = os.read(input_fd, cursor)
os.write(output_fd, half_data)
os.close(input_fd)
os.close(output_fd)
