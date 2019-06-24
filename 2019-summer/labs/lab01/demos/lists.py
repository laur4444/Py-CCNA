#!/usr/bin/env python3

l1 = [1, 2, 3]
l2 = ['python', 3.14, l1]

print(l2)
print(l2[:])

l2[0] = 'py'
print('first element: ', l2[0])
print('last element: ', l2[-1])

for i in l2:
    print(i)

for i in range(0, 3):
    print(i)

print('py' in l2)

l1[1] = 'x'
print(l1)

t = (1, 'x', l1)
print(t)
t[2] = l2

# range(x, y) simuleaza pasii de la x la y-1
numberList = list(range(0, 10))
print(numberList)

# insert(i, x) insereaza valoarea x la pozitia p
numberList.insert(2, 10)
numberList.insert(2, -100)
print(numberList)

# remove(x) elimina din lista toate elementele egale cu x
numberList.remove(10)
print(numberList)

# append(x) adauga x la finalul listei
numberList.append(-11)
print(numberList)

# sort() sorteaza lista
numberList.sort()
print(numberList)

# pop() elimina ultimul element din lista
numberList.pop()
print(numberList)

# reverse() inverseaza ordinea elementelor din lista
numberList.reverse()
print(numberList)
