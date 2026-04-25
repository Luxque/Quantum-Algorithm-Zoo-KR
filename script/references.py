import sys


def read_lines(filename: str) -> list[str]:
    lines = None
    with open(filename, 'r') as file:
        lines = file.read().split('\n')

    return lines

def write_lines(filename: str, lines: list[str]) -> None:
    with open(filename, 'w') as file:
        file.write("# 참고문헌\n\n")
        for line in lines:
            if line.isdigit():
                file.write("#### ")
            file.write(f"{line}\n")

    return


def main() -> None:
    if len(sys.argv) != 2:
        raise RuntimeError("There must be one argument for the file to read.")

    filename = sys.argv[1]
    lines = read_lines(filename)
    write_lines(filename, lines)

    return

if __name__ == '__main__':
    main()
