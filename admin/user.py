class User:
    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")












#user1.increment_login_attempts()
#user1.increment_login_attempts()
#user1.increment_login_attempts()
#user1.increment_login_attempts()
#user1.increment_login_attempts()


#print(f"Login attempts: {user1.login_attempts}")


#user1.reset_login_attempts()


#print(f"Login attempts after reset: {user1.login_attempts}")



#user1 = User("Pasi", "Partanen", 67, "Helsinki", "pasi@example.com")
#user2 = User("Pekka", "Peto", 30, "Porvoo", "pekkapeto@example.com")
#user3 = User("Teppo", "Tervanen", 76, "Kuopio", "teppo@example.com")


#user1.describe_user()
#user1.greet_user()

#user2.describe_user()
#user2.greet_user()

#user3.describe_user()
#user3.greet_user()