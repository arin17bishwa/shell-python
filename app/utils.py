import os
import subprocess
from functools import lru_cache


@lru_cache(maxsize=100)
def _get_command_path(q: str) -> str:
    for directory_path in os.environ.get('PATH').split(os.pathsep):
        if os.path.exists(directory_path) and (q in os.listdir(directory_path)):
            return os.path.join(directory_path, q)
    return ''


def parse_command(command_str: str) -> list[str]:
    command_list: list[str] = []
    curr: list[str] = []
    quote: list[str] = []
    for ch in command_str.strip().replace("''", ""):

        if ch == ' ':
            if quote:
                quote.append(ch)
            elif curr:
                command_list.append(''.join(curr))
                curr = []
        elif ch == "'":
            # opening quote
            if not quote:
                quote.append(ch)
            else:
                command_list.append(''.join(quote[1:]))
                quote = []
        elif quote:
            quote.append(ch)
        else:
            curr.append(ch)
    if curr:
        command_list.append(''.join(curr))
    return command_list


def execute_file(args: list[str]):
    _ = subprocess.run(args)
