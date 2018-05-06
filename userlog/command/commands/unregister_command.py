from userlog.command.command_result import CommandResult
from userlog.user.user_manager import UserManager


class UnregisterCommand:

    def __init__(self, command_manager):
        self.command_manager = command_manager
        self.name = "unregister"
        self.aliases = ["unreg", "remove"]
        self.description = "Unregister a user."
        self.usage = "unregister"

    def execute(self, args):
        name = input("Name: ")

        if UserManager.user_exists(name):
            user = UserManager.get_user(name)
            UserManager.users.remove(user)
            print("User successfully unregistered!")
        else:
            print("User not found.")
        return CommandResult.success
