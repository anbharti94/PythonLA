#! /usr/bin/env python3.7

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file_name',help='the file to read')
parser.add_argument('line_number', type=int, help='the line number to get shown')

args = parser.parse_args()

try:
    with open(args.file_name, 'r') as f:
        lines = f.readlines();
    line = lines[args.line_number - 1]
except IndexError:
    print(f"Error: Line doesn't exists")
except IOError:
    print(f"Error: {err}")
else:
    print(line)
