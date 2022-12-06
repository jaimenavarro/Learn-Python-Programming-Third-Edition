
text_separator = '############################'


################################################################
# Variable positions parameters
################################################################
def function_variable_position_parameter(*parameters):  # Variable positions parameters
    print(type(parameters))
    for i in parameters:
        print(i)


arguments = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # positions arguments
function_variable_position_parameter(1, 2, 3, 4, 5, 6, 7, 8, 9)

print(text_separator)
function_variable_position_parameter(*arguments)  # Iterable unpacking arguments


################################################################
# Variable keyword parameters
################################################################
def function_variable_keyword_parameter(**kwargs):
    print(type(kwargs))
    for k, v in kwargs.items():
        print(k, v)


print(text_separator)
function_variable_keyword_parameter(a=1, b=2)  # Variable keyword arguments

print(text_separator)
arguments = dict(a=1, b=2)
function_variable_keyword_parameter(**arguments)  # Dict unpacking arguments
