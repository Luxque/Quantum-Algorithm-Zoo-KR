from tabulate import tabulate
import sys


def read_csv(filename: str) -> tuple[list[str], list[int], list[str], list[int]]:
    lines = None
    with open(filename, 'r') as file:
        lines = file.read().split('\n')[:-1]

    words_eng, width_eng = [], []
    words_kor, width_kor = [], []

    for line in lines:
        word_pair = line.split(',')
        
        words_eng.append(word_pair[0])
        width_eng.append(len(word_pair[0]))
        words_kor.append(word_pair[1])
        width_kor.append(2 * len(word_pair[1]) - word_pair[1].count(' '))

    return (words_eng, width_eng, words_kor, width_kor)

def write_table(glossary: tuple[list[str], list[int], list[str], list[int]]) -> None:
    header_width_eng = 2 * len("영어")
    header_width_kor = 2 * len("한국어")

    max_width_eng = max(header_width_eng, max(glossary[1]))
    max_width_kor = max(header_width_kor, max(glossary[3]))

    with open('./source/appendix/glossary.md', 'w') as file:
        file.write("# 용어\n\n")
        file.write(f"| 영어 {' '*(max_width_eng-header_width_eng-1)} | 한국어 {' '*(max_width_eng-header_width_kor-1)} |\n")
        file.write(f"|:{'-'*max_width_eng}:|:{'-'*max_width_kor}:|\n")

        for i in range(len(glossary[0])):
            this_word_eng, this_width_eng = glossary[0][i], glossary[1][i]
            this_word_kor, this_width_kor = glossary[2][i], glossary[3][i]

            file.write(f"| {this_word_eng}{' '*(max_width_eng-this_width_eng)} | {this_word_kor}{' '*(max_width_kor-this_width_kor)} |\n")

    return


def main() -> None:
    if len(sys.argv) != 2:
        raise RuntimeError("There must be one argument for the file to read.")
    
    filename = sys.argv[1]
    glossary = read_csv(filename)
    table = write_table(glossary)

    return

if __name__ == '__main__':
    main()
