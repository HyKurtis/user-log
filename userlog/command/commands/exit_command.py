from userlog.command.command_result import CommandResult

class ExitCommand:

    def __init__(self, command_manager):
        self.command_manager = command_manager
        self.name = "exit"
        self.aliases = ["leave", "stop"]
        self.description = "Exit the program."
        self.usage = "exit"

    def execute(self, args):
        self.command_manager.loop = False
        print("Exiting program...")
        return CommandResult.success
