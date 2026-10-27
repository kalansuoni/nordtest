def make_sandwich(*items):
    print("\nMaking a sandwich with:")

    for item in items:
        print(f"- {item}")


#sandwich with 2 items
make_sandwich("ham", "cheese")

#sandwich with 3 items
make_sandwich("turkey", "lettuce", "tomato")

#sandwich with 5 items
make_sandwich("chicken", "bacon", "lettuce", "tomato", "mayo")