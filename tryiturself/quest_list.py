with open('guest_book.txt', 'w') as file_object:
    while True:
        name = input("Enter your name (or 'quit' to exit): ")

        if name.lower() == 'quit':
            break

        file_object.write(name + "\n")
        print(f"Hello, {name}! Your name has been added to the guest book.")