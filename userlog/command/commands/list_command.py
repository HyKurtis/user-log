from userlog.command.command_result import CommandResult
from userlog.user_manager import UserManager


class ListCommand:

    def __init__(self, command_manager):
        self.command_manager = command_manager
        self.name = "list"
        self.aliases = ["viewall"]
        self.description = "List all registered users."
        self.usage = "list"

    def execute(self, args):
        names = []

        if UserManager.users:
            for user in UserManager.users:
                names.append(user.name)

            print("Users: " + ", ".join(names))
        else:
            print("There are no registered users.")
        return CommandResult.success
