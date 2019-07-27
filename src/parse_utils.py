from itertools import islice, compress, chain
from csv import reader
from datetime import datetime
from collections import namedtuple

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


def iter_files(file_names, class_names, parsers_tuple, rowcount):
    for filename, class_name, parser in zip(file_names, class_names,  parsers_tuple):
        file_iter = iter_file(filename, class_name, parser)
        print(filename)
        for _ in range(rowcount):
            print(next(file_iter))
        print()

# -------------- Goal_2 --------------
# chained 4 data rows from raw extract
# chained headers from raw header extract
# chained truth values of parsers compressed
# compress chained headers
# create named tuple based on chained compressed chained header
# compressed raw chained data rows with chained parser compress
# return named combined tuple with combined row


def create_combined_named_tuple_class(file_names, compress_key):
    # you need parsers so you can compress remove the extra ssn keys in the named tuple
    compress_fields = chain.from_iterable(compress_key)
    # print(len(list(compress_fields)))
    zipped_tuple_headers = chain.from_iterable(header_extract(file_name) for file_name in file_names)
    # print(len(list(zipped_tuple_headers)))
    compressed_headers = compress(zipped_tuple_headers, compress_fields)
    # print(list(compressed_headers))
    return namedtuple('Data', compressed_headers)


def iter_combined_files_data_row(file_names, class_names, parsers, compress_key):
    # you need parsers so you can compress remove the extra ssn keys in the named tuple
    compress_fields = tuple(chain.from_iterable(compress_key))

    # chain together all 4 named tuples into one tuple
    # zip(*... this is unpacking the named tuples into a single tuple
    # zipped_tuples returns a tuple of named tuples a row each from 4 files
    zipped_row_tuples = zip(*(iter_file(file_name, class_name, parser)
                            for file_name, class_name, parser in zip(file_names, class_names, parsers)))
    # print(next(zipped_row_tuples))
    merged_row = (chain.from_iterable(zipped_row_tuple) for zipped_row_tuple in zipped_row_tuples)
    for row in merged_row:
        compressed_row = compress(row, compress_fields)
        yield tuple(compressed_row)


def iter_combined_files(file_names, class_names, parsers, compress_key):
    combined_nt = create_combined_named_tuple_class(file_names, compress_key)
    compress_fields = tuple(chain.from_iterable(compress_key))
    zipped_row_tuples = zip(*(iter_file(file_name, class_name, parser)
                              for file_name, class_name, parser in zip(file_names, class_names, parsers)))
    merged_row = (chain.from_iterable(zipped_row_tuple) for zipped_row_tuple in zipped_row_tuples)
    for row in merged_row:
        compressed_row = compress(row, compress_fields)
        yield combined_nt(*compressed_row)

