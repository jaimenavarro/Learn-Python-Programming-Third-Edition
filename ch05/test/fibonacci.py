# The problem is the following: write a function that returns the terms of
# the sequence 0 1 1 2 3 5 8 13 21 ..., up to some limit, N
# F(0) = 0, F(1) = 1 and, for any n > 1, F(n) = F(n-1) + F(n-2)

def fibonacci_list(n):
    result = []
    for i in range(n+1):
        if i == 0:
            result.append(0)
        elif i == 1:
            result.append(1)
        else:
            result.append(sum(result[-2:]))  # result[i - 1] + result[i - 2]
    return result


print(fibonacci_list(0))
print(fibonacci_list(1))
print(fibonacci_list(2))
print(fibonacci_list(10))

print("################################################################")


def fibonacci_generator(n):
    n_0, n_1 = 0, 1
    for i in range(n+1):
        if i == 0:
            yield 0
        elif i == 1:
            yield 1
        else:
            yield n_0 + n_1
            n_0, n_1 = n_1, n_0 + n_1


print(list(fibonacci_generator(0)))
print(list(fibonacci_generator(1)))
print(list(fibonacci_generator(2)))
print(list(fibonacci_generator(10)))

print("################################################################")