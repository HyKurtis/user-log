from userlog.command.command_manager import CommandManager
from userlog.user_manager import UserManager

user_manager = UserManager()
command_manager = CommandManager()


def start_command_loop():
    command_manager.handle_input("help")

    while True:
        command_input = input("> ")
        command_manager.handle_input(command_input)


if __name__ == "__main__":
    start_command_loop()