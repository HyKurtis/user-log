class UserManager:
    users = []

    def load_users(self):
        return

    @staticmethod
    def get_user(name):
        for user in UserManager.users:
            if str.lower(user.name) == str.lower(name):
                return user

    @staticmethod
    def user_exists(name):
        user = UserManager.get_user(name)
        return user is not None
