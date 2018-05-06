from command.command_result import CommandResult
from user_manager import UserManager
from user import User


class RegisterCommand:

    def __init__(self, command_manager):
        self.command_manager = command_manager
        self.name = "register"
        self.aliases = ["reg", "add"]
        self.description = "Register a user."
        self.usage = "register"

    def execute(self, args):
        name = input("Name: ")
        user = User(name)

        for key in user.info:
            value = input(str.title(key) + ": ")
            user.set_value(key, value)

        UserManager.users.append(user)
        print("User successfully registered!")
        return CommandResult.success
