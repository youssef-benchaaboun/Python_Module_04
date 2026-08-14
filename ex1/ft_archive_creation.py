import sys
import typing


def read_file(arguments: list[str]) -> tuple[bool, str]:
    if len(arguments) != 2:
        print(f"Usage: {arguments[0]} <file>")
        return False, ""

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{arguments[1]}'")

    try:
        file: typing.IO[str] = open(arguments[1], "r")
    except OSError as error:
        print(f"Error opening file '{arguments[1]}': {error}")
        return False, ""

    content = file.read()

    print("---")
    print(content)
    print("---")

    file.close()
    print(f"File '{arguments[1]}' closed.")

    return True, content


def transfer_data(content: str) -> str:
    lines = content.splitlines()
    return "\n".join(line + "#" for line in lines)


def write_file(file_path: str, content: str) -> bool:
    if len(file_path) == 0:
        print("Not saving data.")
        return False

    try:
        file: typing.IO[str] = open(file_path, "w")
    except OSError as error:
        print(f"Error opening file '{file_path}': {error}")
        return False

    print(f"Saving data to '{file_path}'")

    try:
        file.write(content)
    except OSError as error:
        print(f"Error writing file '{file_path}': {error}")
        file.close()
        return False

    file.close()
    print(f"Data saved in file '{file_path}'.")
    return True


def main() -> None:
    success, content = read_file(sys.argv)

    if success is False:
        return

    new_content = transfer_data(content)
    print("Transform data:")
    print("---")
    print(new_content)
    print("---")

    file_path = input("Enter new file name (or empty): ")
    write_file(file_path, new_content)


if __name__ == "__main__":
    main()
