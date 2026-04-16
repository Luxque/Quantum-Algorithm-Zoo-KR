import sys


def read_lines(filename: str) -> list[str]:
    lines = None
    with open(filename, 'r') as file:
        lines = file.read().split('\n')

    return lines

def write_lines(filename: str, lines: list[str]) -> None:
    with open(filename, 'w') as file:
        for line in lines:
            print(line)
            if line.isdigit():
                file.write("#### ")
            file.write(f"{line}\n")

    return


def main() -> None:
    if len(sys.argv) < 2:
        raise RuntimeError("There must be at least one argument for the file to edit.")

    filenames = sys.argv[1:]
    for filename in filenames:
        lines = read_lines(filename)
        write_lines(filename, lines)

    return

if __name__ == '__main__':
    main()
