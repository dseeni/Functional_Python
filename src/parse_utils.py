from itertools import islice, compress, chain
from csv import reader
from datetime import datetime
from collections import namedtuple
from itertools import starmap

# -------------- Goal_1 --------------
# f to open file read lines -> yield line - Done
# f open files and read n lines -> yield lines - Done
# extract header of file -> return header tuple - Done
# create named tuple based on header -> return named tuple - Done
# date formatter -> returns date obj with proper format - Done
# zip_data_key -> returns data row zipped with parse key - Done
# cast row based on zip type key and row, as well as date format func -> return clean row tuple
# iter file takes clean row and named tuple -> returns instanced named tuple with clean data


# read lines from csv
def csv_reader(file_name):
    with open(file_name) as f:
        rows = reader(f, delimiter=',', quotechar='"')
        yield from rows


# read n lines from a single file
def row_csv_extract(file, lines: int):
    for row in islice(csv_reader(file), lines):
        yield row


# read n lines from multiple files
def rows_csv_extract(file_names, lines: int):
    for file in file_names:
        for row in islice(csv_reader(file), lines):
            yield row


# extract header row
def header_extract(file_name):
    return tuple(next(csv_reader(file_name)))


def data_row_extract(file_name):
    data_rows = csv_reader(file_name)
    next(data_rows)
    yield from data_rows


# class_name = name of the file personal_info, employment, etc
def create_named_tuple_class(class_name, file_name):
    fields = header_extract(file_name)
    return namedtuple(class_name, fields)


def zip_type_key(data_row, type_key):
    return tuple(zip(data_row, type_key))


# cast row based on zip type key and row, as well as date format func -> return clean row tuple
def cast_zipped_row(zipped_row):
    castedrow = tuple(parse_fn(value) for value, parse_fn in zipped_row)
    return castedrow


def parse_date(value, *, fmt='%Y-%m-%dT%H:%M:%SZ'):
    return datetime.strptime(value, fmt)


def iter_file(fname, class_name, parser):
    nt_class = create_named_tuple_class(class_name, fname)
    for row in data_row_extract(fname):
        parsed_data = cast_zipped_row(zip_type_key(row, parser))
        yield nt_class(*parsed_data)


# -------------- Goal_2 --------------
# chained 4 data rows from raw extract
# chained headers from raw header extract
# chained truth values of parsers compressed
# compress chained headers
# create named tuple based on chained compressed chained header
# compressed raw chained data rows with chained parser compress
# return named combined tuple with combined row

def combined_data_row_extract(file_names):
    # print([data_row_extract(file_name) for file_name in file_names])
    combined_data_rows = chain(*(data_row_extract(file_name) for file_name in file_names))
    yield from combined_data_rows


def flatten_combined_data_rows(combined_data_rows):
    yield chain.from_iterable(next(i) for i in combined_data_rows)

# def compress_chained_keys(parsers, parsers_compress):
#     chained_parsers = chain(*parsers)
#     chained_parsers_compressors = chain(*parsers_compress)
#     return compress(chained_parsers, chained_parsers_compressors)


def iter_combine(fnames, class_names, parsers):
    pass
