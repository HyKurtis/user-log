from userlog.command.command_result import CommandResult
from userlog.user_manager import UserManager


class UpdateCommand:

    def __init__(self, command_manager):
        self.command_manager = command_manager
        self.name = "update"
        self.aliases = ["editinfo", "updateinfo"]
        self.description = "Update a user's information."
        self.usage = "update"

    def execute(self, args):
        name = input("Name: ")

        if UserManager.user_exists(name):
            user = UserManager.get_user(name)
            key = input("Info Type: ")

            if user.key_exists(key):
                value = input("Value: ")
                user.set_value(key, value)
                print("Updated value '" + key + "' successfully!")
            else:
                print("Value '" + key + "' is not valid.")
        return CommandResult.success
