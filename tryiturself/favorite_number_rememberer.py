import json

filename = 'favorite_numberer.json'

try:
    with open(filename) as file_object:
        favorite_number = json.load(file_object)

except FileNotFoundError:
    favorite_number = input("What is your favorite number? ")

    with open(filename, 'w') as file_object:
        json.dump(favorite_number, file_object)

    print("I'll remember your favorite number when you come back!")

else:
    print(f"I know your favorite number! It's {favorite_number}.")
