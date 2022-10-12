# !usr/bin/env python3

from typing import NoReturn

from gendiff.cli import parse_arguments
from gendiff.file_processor.gendiff import generate_diff


def main() -> NoReturn:
    """
    Description:
    ---
        Program entry point.

    Return:
    ---
        Output the result of the generate_diff() function.
    """
    args = parse_arguments()
    try:
        print(
            generate_diff(args.first_file, args.second_file, args.format)
        )
    except Exception as error:
        print(error)


if __name__ == '__main__':
    main()
