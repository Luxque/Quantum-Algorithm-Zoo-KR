"""Module for formatting and processing lines from a reference list."""

import sys


def read_lines(filename: str) -> list[str]:
    """Read and split lines from the specified line.

    Args:
        filename: The path to the files to be read.
    
    Returns:
        A list of strings representing each line in the file.
    """

    lines = None
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.read().split('\n')

    return lines


def write_lines(filename: str, lines: list[str]) -> None:
    """Format and write lines back to the with reference headers.

    Args:
        filename: The path to the file to be written.
        lines: A list of strings to be processed and written.
    """

    with open(filename, 'w', encoding='utf-8') as file:
        file.write("# 참고문헌\n\n")
        for line in lines:
            if line.isdigit():
                file.write("#### ")
            file.write(f"{line}\n")

    return


def main() -> None:
    """Execute the main program."""
    
    if len(sys.argv) != 2:
        raise RuntimeError("There must be one argument for the file to read.")

    filename = sys.argv[1]
    lines = read_lines(filename)
    write_lines(filename, lines)

    return


if __name__ == '__main__':
    main()
