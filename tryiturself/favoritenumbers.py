favorite_numbers = {
    "Oliver": [9, 19, 29],
    "Pasi": [12, 22, 2],
    "Teppo": [3, 13, 23],
    "Masa": [25, 5, 15],
    "Sami": [10, 1, 11]
}

for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are:")

    for number in numbers:
        print(f" {number}")

    print()