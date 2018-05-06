from command.command_result import CommandResult
from command.commands.help_command import HelpCommand
from command.commands.register_command import RegisterCommand
from command.commands.unregister_command import UnregisterCommand
from command.commands.list_command import ListCommand
from command.commands.info_command import InfoCommand
from command.commands.update_command import UpdateCommand


class CommandManager:

    commands = []

    def __init__(self):
        self._register_command(HelpCommand(self))
        self._register_command(RegisterCommand(self))
        self._register_command(UnregisterCommand(self))
        self._register_command(ListCommand(self))
        self._register_command(InfoCommand(self))
        self._register_command(UpdateCommand(self))

    def _get_command(self, name):
        name = str.lower(name)

        for command in self.commands:
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

    def handle_input(self, command_input):
        strings = str(command_input).split()

        if strings:
            name = strings[0]
            command = self._get_command(name)

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
