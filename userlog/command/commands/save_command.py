from userlog.command.command_result import CommandResult
from userlog.user.user_manager import UserManager

class SaveCommand:

    def __init__(self, command_manager):
        self.command_manager = command_manager
        self.name = "save"
        self.aliases = ["export"]
        self.description = "Save changes."
        self.usage = "save"

    def execute(self, args):
        print("Saving changes...")
        UserManager.save()
        print("Changes saved!")
        return CommandResult.success
