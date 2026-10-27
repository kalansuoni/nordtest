from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


# 6-sided die
print("Rolling a 6-sided die 10 times:")
die_6 = Die()

for _ in range(10):
    die_6.roll_die()

# 10-sided die
print("\nRolling a 10-sided die 10 times:")
die_10 = Die(10)

for _ in range(10):
    die_10.roll_die()

# 20-sided die
print("\nRolling a 20-sided die 10 times:")
die_20 = Die(20)

for _ in range(10):
    die_20.roll_die()