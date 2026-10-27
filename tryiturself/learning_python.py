
with open('learning_python.txt') as file_object:
    contents = file_object.read()

print("Reading the entire file:")
print(contents)


with open('learning_python.txt') as file_object:
     lines = file_object.readlines()

print("\nReading the file line by line:")
for line in contents.splitlines():
     print(line.replace('Python', 'C').rstrip())