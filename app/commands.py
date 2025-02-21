import os
import sys
from functools import lru_cache
from pathlib import Path


def _exit(args: list[str]):
    exit_status = int(args[1])
    sys.exit(exit_status)


def _echo(args: list[str]):
    print(' '.join(args[1:]))


def _type(args: list[str]):
    @lru_cache(maxsize=100)
    def _get_command_path(q: str) -> str:
        for directory_path in os.environ.get('PATH').split(os.pathsep):
            if os.path.exists(directory_path) and (q in os.listdir(directory_path)):
                return os.path.join(directory_path, q)
        return ''

    query = args[1]

    if query in COMMAND_MAPPING:
        print(f'{query} is a shell builtin')
    elif _get_command_path(query):
        print(f'{query} is {_get_command_path(query)}')
    else:
        print(f'{query}: not found')


def _pwd(*args):
    print(os.getcwd())


def _cd(args: list[str]):
    arg_path = args[1]
    if arg_path == '~':
        arg_path = str(Path.home())
    if not os.path.exists(arg_path):
        print(f'cd: {arg_path}: No such file or directory')
        return

    os.chdir(arg_path)


COMMAND_MAPPING: dict = {
    'echo': _echo,
    'exit': _exit,
    'type': _type,
    'pwd': _pwd,
    'cd': _cd,
}
