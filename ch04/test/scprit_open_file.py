
file_name = input()
print("Opening file: ", file_name)
file = open(file_name, 'x')


def write_line(text):
    file.write(text)
    file.write('\n')
    file.flush()


def read_from_file():
    text = file.readline()
    return text


while (line := input()) != '':
    write_line(line)
    print(line)
else:
    print(f'Close file {file_name=}')
    file.close()


print("Opening file: ", file_name)
file = open(file_name, 'rt')
print(f'Reading file {file_name=}')
while (line := read_from_file()) != '':
    print(line)


# file.write(input())
# file.close()
# print("File opened")
