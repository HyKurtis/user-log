from userlog.command.command_result import CommandResult

class HelpCommand:

    def __init__(self, command_manager):
        self.command_manager = command_manager
        self.name = "help"
        self.aliases = ["?"]
        self.description = "Show this help message."
        self.usage = "help"

    def execute(self, args):
        for command in self.command_manager.commands:
            print(command.usage + " - " + command.description)
        return CommandResult.success
