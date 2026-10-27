while True:
    age = input("Enter your age (or 'quit' to stop): ")

    if age == "quit":
        break

    age = int(age)

    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")