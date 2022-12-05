from itertools import count
from itertools import compress
from itertools import permutations

text_separator = '###############################################'

# Example of using count() function
for i in count(2, 2):
    print(i)
    if i >= 10:
        break

print(text_separator)
for i in count(1, 1):
    print(i)
    if i >= 10:
        break

# Example of using compress() function
print(text_separator)
data = range(10)
even_selector = [1, 0] * 10
odd_selector = [0, 1] * 10

print(even_selector)
print(odd_selector)

even_numbers = list(compress(data, even_selector))
odd_numbers = list(compress(data, odd_selector))

print(even_numbers)
print(odd_numbers)


# Example of using permutations() function
print(text_separator)
permutations = permutations('ABC')
print(type(permutations))
for i in permutations:
    print(i)

