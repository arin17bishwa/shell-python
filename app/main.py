import sys


def main():
    command_mapping: dict = {
        'echo': _echo,
        'exit': _exit,
    }

    while True:
        sys.stdout.write("$ ")
        command_str: str = input()
        if not command_str:
            pass
        command_args = command_str.split()
        command = command_args[0]
        command_func = command_mapping.get(command)

        if not command_func:
            print(f"{command}: command not found")
        else:
            command_func(command_args)


def _exit(args:list[str]):
    exit_status = int(args[1])
    sys.exit(exit_status)


def _echo(args:list[str]):
    print(' '.join(args[1:]))


if __name__ == "__main__":
    main()
