from itertools import count

text_separator = '###############################################'

for i in count(2, 2):
    print(i)
    if i >= 10:
        break

print(text_separator)
for i in count(1, 1):
    print(i)
    if i >= 10:
        break