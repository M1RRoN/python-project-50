import argparse

from gendiff.formatters.tree_render import FORMATS, DEFAULT_FORMAT


def parse_arguments() -> argparse.Namespace:
    """
    Description:
    ---
        Parses the data entered in the console to run the program.

    Parameters:
    ---
        - first_file (str): First file for comparison.
        - second_file (str): Second file for comparison.

        - format (str): Format for comparison (default: stylish).

    Return:
    ---
        args (Namespace): Entered values.
    """
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')

    parser.add_argument('first_file')
    parser.add_argument('second_file')

    parser.add_argument(
        '-f', '--format',
        help='set format of output (default: stylish)',
        choices=FORMATS,
        default=DEFAULT_FORMAT
    )

    args = parser.parse_args()

    return args
