sandwich_orders = [
    "pastrami",
    "tuna",
    "ham",
    "pastrami",
    "turkey",
    "grilled cheese",
    "pastrami",
    "chicken"
]

finished_sandwiches = []

print("The deli has run out of pastrami.\n")


while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")


while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)

    print(f"I made your {current_sandwich} sandwich.")

    finished_sandwiches.append(current_sandwich)


print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()} Sandwich")