import sys


def main():
    while True:
        sys.stdout.write("$ ")
        command: str = input()
        if command == 'exit 0':
            sys.exit(0)
        print(f"{command}: command not found")


if __name__ == "__main__":
    main()
