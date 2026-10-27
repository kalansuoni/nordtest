
pizzas = ['Margherita', 'Hawaii', 'Frozen', 'Pepperoni']
friend_pizzas = ['Margherita', 'Hawaii', 'Frozen', 'Tuna']
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza.")
print('I like pizza alot.')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print("My friends favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza.title())