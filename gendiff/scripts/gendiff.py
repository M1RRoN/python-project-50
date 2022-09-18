#!/usr/bin/env python3
from gendiff.engine import run_gendiff
import argparse


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument("-f", '--format', metavar='FORMAT', help="set format of output")
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    args = vars(parser.parse_args())
    file1 = args['first_file']
    file2 = args['second_file']
    run_gendiff(file1, file2)


if __name__ == '__main__':
    main()
