import sys


def _exit(args: list[str]):
    exit_status = int(args[1])
    sys.exit(exit_status)


def _echo(args: list[str]):
    print(' '.join(args[1:]))


def _type(args: list[str]):
    query = args[1]
    # print(COMMAND_MAPPING)
    if query in COMMAND_MAPPING:
        print(f'{query} is a shell builtin')
    else:
        print(f'{query}: not found')


COMMAND_MAPPING: dict = {
    'echo': _echo,
    'exit': _exit,
    'type': _type,
}
