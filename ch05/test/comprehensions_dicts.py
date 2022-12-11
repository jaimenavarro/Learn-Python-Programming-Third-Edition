from string import ascii_lowercase
for k, c in enumerate(ascii_lowercase, 1):
    print(k, c)

lettermap = {c: k for k, c in enumerate(ascii_lowercase, 1)}

print(type(lettermap))
print(lettermap)

lettermap = dict((c, k) for k, c in enumerate(ascii_lowercase, 1))

print(type(lettermap))
print(lettermap)

print("################################################################")
a = ('a', 1)

print(type({a}))
print(dict((k, c) for k, c in enumerate(ascii_lowercase, 1)))

print(dict(a=1, b=2, c=3))
print(dict([('a', 1), ('b', 2), ('c', 3)]))
