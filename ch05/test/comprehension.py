square = list()
for i in range(10):
    square.append(i ** 2)
    print(i)

print(square)

print(list(map(lambda x: x ** 2, range(10))))

print([n ** 2 for n in range(10)])
s = (n ** 2 for n in range(10))
print(type(s))
print(next(s))
print(s.__iter__().__next__())
print(s.__next__())


print("################################################################################")

print(list(map(lambda x: x ** 2, filter(lambda y: y <= 5, range(10)))))
print(type(map(lambda x: x ** 2, filter(lambda y: y <= 5, range(10)))))

print([n ** 2 for n in range(10) if n <= 5])
print(type(n ** 2 for n in range(10) if n <= 5))

print("################################################################################")

a = 'abcdef'
pairs = []
for i in range(6):
    for j in range(i, 6):
        print(i, j, "|", a[i], a[j])
        pairs.append((a[i], a[j]))

print(pairs)

pairs = [(a[i], a[j]) for i in range(6) for j in range(i, 6) if 0 <= j <= 5]

print(pairs)


print("################################################################################")

from math import sqrt

mx = 10
result = []
for i in range(mx):
    for j in range(i, mx):
        if i > 0 and sqrt(i**2 + j**2).is_integer():
            print(i, j, sqrt(i**2 + j**2))
            result.append((i, j, sqrt(i**2 + j**2)))


print(result)

result = [(i, j, sqrt(i**2 + j**2))
          for i in range(mx)
          for j in range(i, mx)
          if i > 0 and sqrt(i**2 + j**2).is_integer()]

print(result)

result = [(i, j, int(c))
          for i in range(1, mx)
          for j in range(i, mx)
          if i > 0 and (c := sqrt(i**2 + j**2)).is_integer()]

print(result)

t = (0, 1, 2, 4)
print(t[:2])
print(t[0:2] + (1,))



