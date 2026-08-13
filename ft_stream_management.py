import sys
import typing


def read_file(arguments: list[str]) -> tuple[bool, str]:
    if len(arguments) != 2:
        sys.stderr.write(f"[STDERR] Usage: {arguments[0]} <file>")
        return False, ""

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{arguments[1]}'")

    try:
        file: typing.IO[str] = open(arguments[1], "r")
    except OSError as error:
        sys.stderr.write(f"[STDERR] Error opening file '{arguments[1]}': {error}")
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
    new_content="\n".join(line + "#" for line in lines)
    print("Transform data:")
    print("---")
    print(new_content)
    print("---")
    return new_content



def write_file(file_path: str, content: str) -> bool:
    if len(file_path) == 0:
        return False

    try:
        file: typing.IO[str] = open(file_path, "w")
    except OSError as error:
        sys.stderr.write(f"[STDERR] Error opening file '{file_path}': {error}")
        return False

    print(f"Saving data to '{file_path}'")

    try:
        file.write(content)
    except OSError as error:
        sys.stderr.write(f"Error writing file '{file_path}': {error}")
        file.close()
        return False

    file.close()
    return True


def main() -> None:

    success, content = read_file(sys.argv)
    if success is False:
        return   
    new_content = transfer_data(content)

    print("Enter new file name (or empty): ",end='')
    sys.stdout.flush()
    file_path = sys.stdin.readline()

    if write_file(file_path, new_content):
        print(f"Data saved in file '{file_path}'.")
    else:
        print("Not saving data.")




if __name__ == "__main__":
    main()