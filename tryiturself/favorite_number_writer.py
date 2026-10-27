import json

favorite_number = input("What is your favorite number? ")

with open('favorite_number.json', 'w') as file_object:
    json.dump(favorite_number, file_object)

print("Your favorite number has been saved.")