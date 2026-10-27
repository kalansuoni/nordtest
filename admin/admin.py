from user import User


class Privileges:
    def __init__(self):
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can edit post",
            "can manage users"
        ]

    def show_privileges(self):
        print("Administrator privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, username, email):
        super().__init__(first_name, last_name, username, email)
        self.privileges = Privileges()