name = input("What is your name? ")

with open('guest.txt', 'w') as file_object:
    file_object.write(name)

print(f"Hello, {name}! Your name has been saved to guest.txt.")