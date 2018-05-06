from userlog.user.storage.user_storage import UserStorage


class UserManager:

    users = []

    def __init__(self):
        UserManager.load()

    @staticmethod
    def save():
        user_storage = UserStorage()
        user_storage.export_to(UserManager.users, 'data.json')

    @staticmethod
    def load():
        user_storage = UserStorage()
        users = user_storage.import_from('data.json')

        for user in users:
            UserManager.users.append(user)

    @staticmethod
    def get_user(name):
        for user in UserManager.users:
            if str.lower(user.name) == str.lower(name):
                return user

    @staticmethod
    def user_exists(name):
        user = UserManager.get_user(name)
        return user is not None
