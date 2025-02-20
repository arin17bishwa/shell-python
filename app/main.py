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
            command_func()


def _exit(*args):
    exit_status = int(args[1])
    print(args)
    sys.exit(0)


def _echo(*args):
    print(' '.join(args[1:]))


if __name__ == "__main__":
    main()
