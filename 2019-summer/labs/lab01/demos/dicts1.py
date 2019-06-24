#!/usr/bin/env python3

d = {
    'Name' : 'Bulbasaur',
    'Pokedex Number' : 1,
    'Type' : ['Grass', 'Poison'],
    'Moves' : {
                1 : 'Tackle',
                5 : 'Vine Whip',
               	9	: 'Leech Seed',
                14 : 'Poison Powder',
                14 : 'Sleep Powder'
              }
    }

print(d)
print(d['Moves'])

for k in d.keys():
    print(k)

for v in d.values():
	print(v)

for t in d.items():
	print(t)
