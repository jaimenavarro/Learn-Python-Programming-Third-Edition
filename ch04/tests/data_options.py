################################
# Tuples examples
################################
a = tuple((1, 2, 3))
b = (1, 2, 3)
print(type(a), type(b))
print(a, b)

###############################
# List examples
###############################
a = list((1, 2, 3))
b = [1, 2, 3]
print(type(a), type(b))
print(a, b)

###############################
# Dict examples
###############################
a = dict(a=1, b=2, c=3)
b = {'a': 1, 'b': 2, 'c': 3}
print(type(a), type(b))
print(a, b)


###############################
# Set examples
###############################
def connection():
    print('Connected to the server')
    con = dict(host='localhost', port=8080)
    return con


print(connection())


