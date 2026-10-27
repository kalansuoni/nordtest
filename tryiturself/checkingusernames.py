current_users = ["admin", "pekka", "oliver", "sara", "sami"]

new_users = ["Oliver", "simo", "PASI", "sara", "teppo"]


current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"Sorry, the username '{user}' has already been used. Please enter a new username.")
    else:
        print(f"The username '{user}' is available.")