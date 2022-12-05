from custom_file.read_file import ReadFile
from custom_file.write_file import WriteFile

################################################################
# Writing files
################################################################
file_name = input()
print("Writing file: ", file_name)
file = WriteFile(file_name)

while (line := input()) != '':
    file.write_line(line)
    print(line)

print(f'Close file {file_name=}')
file.close()


################################################################
# Reading files
################################################################
file = ReadFile(file_name)
print(f'Reading file {file_name=}')
while (line := file.read_line()) != '':
    print(line, end='')

print(f'Close file {file_name=}')
file.close()

