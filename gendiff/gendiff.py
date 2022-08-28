import argparse


def gendiff():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument("-f", '--format', help="set format of output")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()
    print(args.echo)


'''
gendiff -h
usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
  '''
