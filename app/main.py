import sys

from app.commands import COMMAND_MAPPING


def main():
    while True:
        sys.stdout.write("$ ")
        command_str: str = input()
        if not command_str:
            pass
        command_args = command_str.split()
        command = command_args[0]
        command_func = COMMAND_MAPPING.get(command)

        if not command_func:
            print(f"{command}: command not found")
        else:
            command_func(command_args)


if __name__ == "__main__":
    main()
