from command.command_result import CommandResult
from user_manager import UserManager


class InfoCommand:

    def __init__(self, command_manager):
        self.command_manager = command_manager
        self.name = "info"
        self.aliases = ["showinfo"]
        self.description = "View a user's information."
        self.usage = "info"

    def execute(self, args):
        name = input("Name: ")

        if UserManager.user_exists(name):
            user = UserManager.get_user(name)

            for key in user.info:
                value = user.get_value(key)

                if value is not None:
                    print(str.title(key) + ": " + value)
        else:
            print("User not found.")
        return CommandResult.success
