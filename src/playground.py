from itertools import islice
from src.constants import fnames, parsers, class_names
from csv import reader


# read file as csv
def read_file(file_name):
    with open(file_name) as f:
        rows = reader(f, delimiter=',', quotechar='"')
        yield from rows


# read N lines for file in fnames
for file in fnames:
    lines = read_file(file)
    for line in islice(lines, 5):
        print(line)

