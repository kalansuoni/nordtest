rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "mississippi": "united states"
}

#sentence
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print()

#river
print("Rivers:")
for river in rivers.keys():
    print(river.title())

print()

#country
print("Countries:")
for country in rivers.values():
    print(country.title())