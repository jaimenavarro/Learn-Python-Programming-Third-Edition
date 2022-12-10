print("########################### MAP #####################################")
print(list(map(lambda x: (x,), range(10))))
print(list(map(lambda *args: args, range(10))))
print(list(map(lambda x, y: (x, y), range(10), 'abcdefghijklmnop')))
print(list(map(lambda *args: args, range(10), 'abcdefghijklmnop')))

iterator_map = map(lambda *args: args, range(10), 'abcdefghijklmnop')
print(type(next(iterator_map)))
print(next(iterator_map))
print(iterator_map.__next__())

print("########################### ZIP #####################################")
print(list(zip(range(10), 'abcdefghijklmnop', range(5))))
iterator_zip = zip(range(10), 'abcdefghijklmnop', range(5))
print(type(next(iterator_zip)))
print(next(iterator_zip))

a = [10, 2, 3]
b = [4, 9, 6]
c = [7, 8, 9]
print(list(zip(a, b, c)))
print(list(map(lambda x: max(x), zip(a, b, c))))


print("########################### FILTER #####################################")
print(list(filter(lambda x: x % 2 == 0, range(10))))
print(list(filter(id, range(10))))
