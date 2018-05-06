from userlog.command.command_result import CommandResult
from userlog.command.commands.help_command import HelpCommand
from userlog.command.commands.register_command import RegisterCommand
from userlog.command.commands.unregister_command import UnregisterCommand
from userlog.command.commands.list_command import ListCommand
from userlog.command.commands.info_command import InfoCommand
from userlog.command.commands.update_command import UpdateCommand
from userlog.command.commands.exit_command import ExitCommand
from userlog.command.commands.save_command import SaveCommand


class CommandManager:

    commands = []

    def __init__(self):
        self.loop = True

        self._register_command(HelpCommand(self))
        self._register_command(RegisterCommand(self))
        self._register_command(UnregisterCommand(self))
        self._register_command(ListCommand(self))
        self._register_command(InfoCommand(self))
        self._register_command(UpdateCommand(self))
        self._register_command(ExitCommand(self))
        self._register_command(SaveCommand(self))

        self.start_loop()

    @staticmethod
    def _get_command(name):
        name = str.lower(name)

        for command in CommandManager.commands:
            command_name = str.lower(command.name)

            if command_name == name:
                return command

            for command_alias in command.aliases:
                command_alias = str.lower(command_alias)

                if command_alias == name:
                    return command

        return None

    def _register_command(self, command):
        if self._get_command(command.name) is None:
            self.commands.append(command)

    @staticmethod
    def handle_input(command_input):
        strings = str(command_input).split()

        if strings:
            name = strings[0]
            command = CommandManager._get_command(name)

            strings.pop(0)

            if command is not None:
                result = command.execute(strings)

                if result != CommandResult.success:
                    if result == CommandResult.error:
                        print("An error occured. Please tell an administrator.")
                    elif result == CommandResult.bad_usage:
                        print(command.usage)
                return

        print("Unknown command. Try 'help'.")

    def start_loop(self):
        CommandManager.handle_input("help")

        while self.loop:
            command_input = input("> ")
            CommandManager.handle_input(command_input)
