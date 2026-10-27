dream_vacations = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    vacation = input("If you could visit one place in the world, where would you go? ")

    dream_vacations[name] = vacation

    repeat = input("Would you like to let another person respond? (yes/no) ")

    if repeat.lower() == "no":
        polling_active = False

print("\n--- Dream Vacation Poll Results ---")

for name, vacation in dream_vacations.items():
    print(f"{name.title()} would like to visit {vacation.title()}.")