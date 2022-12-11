def function_generator(x):
    for i in range(x):
        yield i**2


g = function_generator(10)
print(type(g))
print(g)
print(g.__next__())
print(next(g))
print(g.__next__())
print(next(g))


print("################################################################")


def function_generator2():
    count = 0
    while True:
        count += 1
        if count <= 10:
            yield count
        else:
            break  # or return


for i in function_generator2():
    print(i)


print("################################################################")

def function_generator_forever():
    count = 0
    value = None
    while True:
        if value is None or count <= 10:
            value = yield count
            print("yield value: ", value)
        else:
            return
        count += 1


generator = function_generator_forever()
print(generator.__next__())
print(generator.send(None))
print(generator.__next__())
print(generator.send(None))
print(generator.__next__())
print(generator.send(None))
print(generator.__next__())
print(generator.send('finish'))
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())