pet1 = {
    "animal": "cat",
    "owner": "Oliver",
    "name": "Nene"
}

pet2 = {
    "animal": "dog",
    "owner": "Pasi",
    "name": "Kamu"
}

pet3 = {
    "animal": "rabbit",
    "owner": "Mia",
    "name": "Pupu"
}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"Pet Name: {pet['name']}")
    print(f"Animal: {pet['animal'].title()}")
    print(f"Owner: {pet['owner']}")
    print()