"""Module for parsing CSV glossaries and generating sorted Markdown table."""

import sys


def parse_csv(filename: str) -> dict[str, str]:
    """Read the given CSV file and parse it into a dictionary of terms.

    Args:
        filename: The path to the CSV files to read.
    
    Returns:
        A dictionary mapping English terms to their Korean translations.
    """

    lines = None
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.read().split('\n')[:-1]

    glossary = {}
    for line in lines:
        english, korean = line.split(',')
        glossary[english] = korean

    return glossary


def sort_keys(glossary: dict[str, str]) -> list[str]:
    """Sort glossary keys case-insensitively.

    Args:
        glossary: The glossary dictionary containing English-Korean paris.

    Returns:
        A sorted list of English keys using case-insensitive comparison.
    """

    return sorted(list(glossary.keys()), key=str.casefold)


def write_output(filename: str, glossary: dict[str, str], keys: list[str]) -> None:
    """Write the sorted glossary back to the CSV and generate a Markdown table.

    Args:
        filename: The path to the original CSV file.
        glossary: The glossary dictionary containing English-Korean paris.
        keys: A sorted list of keys to order the output.
    """

    with open(filename, 'w', encoding='utf-8') as csv_file, \
            open(filename[:-3] + "md", 'w', encoding='utf-8') as md_file:
        md_file.write("| 영어 | 한국어 |\n")
        md_file.write("|:----|:------|\n")

        for key in keys:
            csv_file.write(f"{key},{glossary[key]}\n")
            md_file.write(f"| {key} | {glossary[key]} |\n")

    return


def main() -> None:
    """Execute the main program."""

    if len(sys.argv) != 2:
        raise RuntimeError("There must be one argument for the file to read.")
    
    filename = sys.argv[1]
    if not filename.endswith('.csv'):
        raise RuntimeError("The input must be a CSV file.")

    glossary = parse_csv(filename)
    keys = sort_keys(glossary)
    write_output(filename, glossary, keys)

    return


if __name__ == '__main__':
    main()
