class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant: {self.restaurant_name}")
        print(f"Cuisine: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, additional_customers):
        self.number_served += additional_customers


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = [
            "Vanilla",
            "Chocolate",
            "Strawberry",
            "Mint Chocolate Chip",
            "Cookie Dough"
        ]

    def display_flavors(self):
        print("\nAvailable flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")



ice_cream_stand = IceCreamStand("Sweet Scoops", "Ice Cream")


ice_cream_stand.describe_restaurant()


ice_cream_stand.display_flavors()


restaurant = Restaurant("Pizza Palace", "Italian")


print(f"Customers served: {restaurant.number_served}")


restaurant.number_served = 25
print(f"Customers served: {restaurant.number_served}")


restaurant.set_number_served(50)
print(f"Customers served: {restaurant.number_served}")


restaurant.increment_number_served(30)
print(f"Customers served: {restaurant.number_served}")


restaurant1 = Restaurant("Pizza Palace", "Italian")
restaurant2 = Restaurant("Sushi World", "Japanese")
restaurant3 = Restaurant("Burger House", "American")


restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()