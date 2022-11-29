text_separator = '###############################################'

for i in range(10):
    print(i)

print(text_separator)
surnames = ['Rivest', 'Shamir', 'Adleman']
for i in surnames:
    print(i)

print(text_separator)
for i in enumerate(surnames):
    print(i)
    print(i[0], i[1])

print(text_separator)
for i in enumerate(surnames):
    print(surnames[(i[0])][0], end='')


print(text_separator)
print(text_separator)
people = ['Nick', 'Rick', 'Roger', 'Syd']
ages = [23, 24, 23, 21]
instruments = ['Drums', 'Keyboards', 'Bass', 'Guitar']

for i in zip(people, ages, instruments):
    print(i)
    print(i[0], i[1], i[2])

print(text_separator)
for person, age, instrument in zip(people, ages, instruments):
    print(person, age, instrument)

print(text_separator)
b = b'caca'
for i in b:
    print(chr(i), end='')
