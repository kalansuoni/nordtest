favorite_places = {
    "Pasi": ["Helsinki", "Tokyo", "Paris"],
    "Teppo": ["London", "Rome"],
    "Masa": ["New York", "Toronto", "Vancouver"]
}

for person, places in favorite_places.items():
    print(f"{person}'s favorite places are:")

    for place in places:
        print(f"  - {place}")

    print()