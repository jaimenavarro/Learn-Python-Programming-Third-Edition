"""
This example shows execution a representation of:
    list(map(lambda *a: a, range(100000)))
"""


def function(*a):
    # print(a)
    # print(*a)
    return a


result = []
for i in range(1_000_000):
    result.append(function(i))

print(result)


"""
This example shows execution a representation of:
    list(map(lambda *a: a, range(1000), range(1000)))
"""
#
# result1 = []
# for i in range(1000):
#     for j in range(i, 1000):
#         result1.append(function(i, j))
#
# print(result1)
