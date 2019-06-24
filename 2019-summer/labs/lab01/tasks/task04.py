#!/usr/bin/env python3

'''
	Splits & Joins!
	Sa se transforme o adresa de email de tipul
prenume1_prenume2.nume@yahoo.com in prenume1.nume@gmail.com

Demo:
string = "This\\is\\a\\Windows\\path"
print(string)
print(string.replace('\\', '/').replace('Windows', 'Linux'))
# Pentru a 'modifica' stringul initial folositi urmatoarea instructiune:
# string = string.replace('\\', '/').replace('Windows', 'Linux')
# [Reminder] Strings are immutable!

# _string_.split(_token_) returneaza o lista
url = 'www.google.com'
tokens = url.split('.')
print(tokens)

# '_token_'.join(_list_) returneaza un string
# Obs: .split() are ca argument default caracterul spatiu
function = 'bad~!$@ function name'
f = '_'.join(function.split()[1:]) # Ce credeti ca face [1:]?
print(f)
'''

mail = 'ana_maria.popescu@yahoo.com'