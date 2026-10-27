favorite_languages = {
    "pasi": "python",
    "pekka": "c",
    "sami": "rust",
    "teppo": "python",
}

people_to_poll = ["teppo", "pasi", "oliver", "pekka", "onni", "sami"]

for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for responding to the poll.")
    else:
        print(f"{person.title()}, please take our favorite languages poll!")