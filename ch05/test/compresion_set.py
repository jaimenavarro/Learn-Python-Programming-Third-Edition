word = 'Hello'

a = {c for c in word}
b = set(c for c in word)

print(type(a))
print(a)
print(type(b))
print(b)

