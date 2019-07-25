from itertools import islice
from csv import reader
from datetime import datetime
from collections import namedtuple


# read file as csv
def csv_reader(file_name):
    with open(file_name) as f:
        rows = reader(f, delimiter=',', quotechar='"')
        yield from rows


# read N lines for file in fnames
def row_csv_extract(file_names, lines: int):
    for file in file_names:
        rows = csv_reader(file)
        for row in islice(rows, lines):
            print(row)


# extract header files
def header_extract(file_name):
    with open(file_name) as f:
        file_line = reader(f, delimiter=',', quotechar='"')
        return next(file_line)


def data_row_extract(file_name):
    with open(file_name) as f:
        file_line = reader(f, delimiter=',', quotechar='"')
        # skip the header line
        next(file_line)
        yield next(file_line)


# class_name = name of the file personal_info, employment, etc
def create_named_tuple_class(fname, class_name):
    fields = header_extract(fname)
    return namedtuple(class_name, fields)


def iter_file(fname, class_name, parser):
    nt_class = create_named_tuple_class(fname, class_name)
    reader = csv_reader(fname)
    for row in reader:
        parsed_data = (cast(element, data_type) for element, data_type in zip(row, parser))
        yield nt_class(*parsed_data)



def cast(element, data_type):
    if element is None:
        return None
    elif data_type == float:
        return float(element)
    elif data_type == int:
        return int(element)
    elif data_type == parse_date:
        return parse_date(element)
    else:
        if len(str(element)) is 0:
            return None
        return str(element)


def parse_date(value, *, fmt='%Y-%m-%dT%H:%M:%SZ'):
    return datetime.strptime(value, fmt)
