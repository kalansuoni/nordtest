

person1 = {
    "first_name": "Teppo",
    "last_name": "Tervanen",
    "age": 66,
    "city": "Malta"
}

person2 = {
    "first_name": "Sami",
    "last_name": "Sarvinen",
    "age": 75,
    "city": "London"
}

person3 = {
    "first_name": "Pasi",
    "last_name": "Partanen",
    "age": 22,
    "city": "Stockholm"
}

people = [person1, person2, person3]

for person in people:
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print()