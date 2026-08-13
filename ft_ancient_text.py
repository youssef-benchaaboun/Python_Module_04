import sys
import typing


def read_file(arguments: list[str]) -> None:
    if len(arguments) != 2:
        print(f"Usage: {arguments[0]} <file>")
        return

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{arguments[1]}'")

    try:
        file: typing.IO[str] = open(arguments[1], "r")
    except OSError as error:
        print(f"Error opening file '{arguments[1]}': {error}")
        return

    content = file.read()

    print("---")
    print(content)
    print("---")

    file.close()
    print(f"File '{arguments[1]}' closed.")


if __name__ == "__main__":
    read_file(sys.argv)