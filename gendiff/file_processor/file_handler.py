from os import path


FILEREAD_ERR = '''Failed to open file '{}'.
Please, check that the file path is entered correctly.'''


def explore_file(file_path: str) -> tuple:
    """
    Description:
    ---
        Reads a file and gets the file extension.

    Parameters:
    ---
        - file_path (str): Path to file (absolute or relative).

    Raises:
    ---
        - RuntimeError: Failed to open file.

    Return:
    ---
        content (str): Data from a file as a string.
        file_extension (str): File extension.
    """
    return read_file(file_path), get_file_extension(file_path)


def read_file(file_path: str) -> str:

    try:
        with open(file_path, 'r', encoding='utf-8') as content:
            return content.read()
    except OSError:
        raise RuntimeError(FILEREAD_ERR.format(file_path))


def get_file_extension(file_path: str) -> str:

    _, file_extension = path.splitext(file_path)
    file_extension = file_extension.lower()

    return file_extension
