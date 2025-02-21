import sys

from app.commands import COMMAND_MAPPING
from app.utils import _get_command_path, execute_file


def main():
    while True:
        sys.stdout.write("$ ")
        command_str: str = input()
        if not command_str:
            pass
        command_args = command_str.split()
        command = command_args[0]
        command_func = COMMAND_MAPPING.get(command)

        if command_func:
            command_func(command_args)
        elif _get_command_path(command):
            execute_file(command_args)
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
