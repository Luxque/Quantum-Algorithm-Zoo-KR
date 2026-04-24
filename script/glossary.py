from tabulate import tabulate
import sys


def read_csv(filename: str) -> list[list[str]]:
    lines = None
    with open(filename, 'r') as file:
        lines = file.read().split('\n')[:-1]

    glossary = []
    for line in lines:
        word_pair = line.split(',')
        glossary.append(word_pair)

    return glossary

def write_table(filename: str, glossary: list[list[str]]) -> None:
    headers = ["영어", "한국어"]
    table = tabulate(
        glossary, 
        headers=headers, 
        tablefmt='pipe'
    )

    with open('./source/appendix/glossary.md', 'w') as file:
        file.write("# 용어\n\n")
        file.write(f"{table}\n")

    return


def main() -> None:
    if len(sys.argv) != 2:
        raise RuntimeError("There must be one argument for the file to read.")
    
    filename = sys.argv[1]
    glossary = read_csv(filename)
    table = write_table(filename, glossary)

if __name__ == '__main__':
    main()
