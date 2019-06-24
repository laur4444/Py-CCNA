#!/usr/bin/env python3

var1 = 131
var2 = 56.78
var3 = complex(2, 3)

print(var1, bin(var1), hex(var1), sep = ' ---- ')

print(var1, type(var1))
print(var2, type(var2))
print(var3, type(var3))

var1 = var1 + var2
print(var1, type(var1))

if var1 > var2:
    print('var1 is bigger than var2')
else:
    print('var2 is bigger than var1')

cnt = 0
while cnt < 10:
    if cnt > 1 and not cnt & (cnt - 1):
        print(cnt, 'power of 2')
    elif cnt % 2 == 0:
        print('just an even number')
    else:
        print('just an odd number')
    cnt = cnt + 1

print(2**10, (1<<10), sep = '<->')
print('0xcafebabe' + ' = ' + str(int('0xcafebabe', 16)))
