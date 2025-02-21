import os
import subprocess
from functools import lru_cache


@lru_cache(maxsize=100)
def _get_command_path(q: str) -> str:
    for directory_path in os.environ.get('PATH').split(os.pathsep):
        if os.path.exists(directory_path) and (q in os.listdir(directory_path)):
            return os.path.join(directory_path, q)
    return ''


def execute_file(args: list[str]):
    _ = subprocess.run(args)
