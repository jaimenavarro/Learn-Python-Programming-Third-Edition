# if it's division by [2,n) has a remainder 0, then it's a composite number.
# otherwise it's a prime.

primes = []  # list()
print("Give the range number to look for prime:")
while (numbers := int(input())) >= 10000:
    print("Number is above 10000")
# else:  # while condition is not meet, this is executed
#     numbers = x

for n in range(2, int(numbers)):
    for i in range(2, n):
        if n % i == 0:
            break
    else:  # for iterator is exhausted, this is executed (not if break!)
        primes.append(n)

print(primes)



