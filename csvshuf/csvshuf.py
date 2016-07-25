# -*- coding: utf-8 -*-
"""
Shuffle cells by column in CSV files.

Forked from csvcut (https://gist.github.com/bycoffe/187278)
Improved thanks to http://codereview.stackexchange.com/q/129806/13659
"""


import csv
import sys
import random
import argparse


__version__ = '1.0.1'


def shuffle_sattolo(items):
    """Shuffle items in place using Sattolo's algorithm."""
    _randrange = random.randrange
    for i in reversed(range(1, len(items))):
        j = _randrange(i)  # 0 <= j < i
        items[j], items[i] = items[i], items[j]


def column_list(string):
    """Validate and convert comma-separated list of column numbers."""
    try:
        columns = list(map(int, string.split(',')))
    except ValueError as e:
        raise argparse.ArgumentTypeError(*e.args)
    for column in columns:
        if column < 1:
            raise argparse.ArgumentTypeError(
                'Invalid column {!r}: column numbers start at 1.'
                .format(column))
    return columns


def main():
    parser = argparse.ArgumentParser(description='Shuffle columns in a CSV file')
    parser.add_argument(metavar="FILE", dest='input_file', type=argparse.FileType('r'), nargs='?',
                        default=sys.stdin, help='Input CSV file. If omitted, read standard input.')
    parser.add_argument('-s', '--sattolo',
                        action='store_const', const=shuffle_sattolo,
                        dest='shuffle', default=random.shuffle,
                        help="Use Sattolo's shuffle algorithm.")
    col_group = parser.add_mutually_exclusive_group()
    col_group.add_argument('-c', '--columns', type=column_list,
                           help='Comma-separated list of columns to include.')
    col_group.add_argument('-C', '--no-columns', type=column_list,
                           help='Comma-separated list of columns to exclude.')
    delim_group = parser.add_mutually_exclusive_group()
    delim_group.add_argument('-d', '--delimiter', type=str, default=',',
                             help='Input column delimiter.')
    delim_group.add_argument('-t', '--tabbed', dest='delimiter',
                             action='store_const', const='\t',
                             help='Delimit input with tabs.')
    parser.add_argument('-q', '--quotechar', type=str, default='"',
                        help='Quote character.')
    parser.add_argument('-o', '--output-delimiter', type=str, default=',',
                        help='Output column delimiter.')
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s {version}'.format(version=__version__))
    args = parser.parse_args()

    reader = csv.reader(args.input_file, delimiter=args.delimiter, quotechar=args.quotechar)

    """Get the first row and use it as column headers"""
    headers = next(reader)

    """Create a matrix of lists of columns"""
    table = []
    for c in range(len(headers)):
        table.append([])
    for row in reader:
        for c in range(len(headers)):
            table[c].append(row[c])

    cols = args.columns
    if args.no_columns:
        """If columns to exclude are provided, get a list of all other columns"""
        cols = list(set(range(len(headers))) - set(args.no_columns))
    elif not cols:
        """If no columns are provided all columns will be shuffled"""
        cols = range(len(headers))

    for c in cols:
        if c > len(headers):
            sys.stderr.write('Invalid column {0}. Last column is {1}.\n'.format(c, len(headers)))
            exit(1)
        args.shuffle(table[c - 1])

    """Transpose the matrix"""
    table = zip(*table)

    writer = csv.writer(sys.stdout, delimiter=args.output_delimiter)
    writer.writerow(headers)
    for row in table:
        writer.writerow(row)
