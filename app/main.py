import sys


def main():
    while True:
        sys.stdout.write("$ ")
        command: str = input()
        print(f"{command}: command not found")


if __name__ == "__main__":
    main()
