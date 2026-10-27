from random import sample


lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']


my_ticket = [3, 'B', 7, 'D']

attempts = 0
winning_ticket = []

while winning_ticket != my_ticket:
    winning_ticket = sample(lottery_pool, 4)
    attempts += 1

print(f"My ticket: {my_ticket}")
print(f"Winning ticket: {winning_ticket}")
print(f"It took {attempts} attempts to win!")