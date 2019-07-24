from itertools import islice
from csv import reader
from datetime import datetime


# read file as csv
def read_file(file_name):
    with open(file_name) as f:
        rows = reader(f, delimiter=',', quotechar='"')
        yield from rows


# read N lines for file in fnames
def read_file_rows(file_names, lines: int):
    for file in file_names:
        rows = read_file(file)
        for row in islice(rows, lines):
            print(row)


def header_extract(file_names):
    for file_name in file_names:
        with open(file_name) as f:
            file_line = reader(f, delimiter=',', quotechar='"')
            yield next(file_line)
    # with open(self.filename) as file:
    #     next(file)
    #     data_string = next(file).strip('\n')
    #     self.data_key = data_string.split(',')
    #     self.infer_data_type()


def data_row_extract(file_names):
    for file_name in file_names:
        with open(file_name) as f:
            file_line = reader(f, delimiter=',', quotechar='"')
            next(file_line)
            yield next(file_line)


def cast_data_row(data_row, data_type_key):
    for element, data_key in data_row, data_type_key:
        if element is None:
            return None
        elif data_key == 'float':
            return float(element)
        elif data_key == 'int':
            return int(element)
        else:
            if len(str(element)) is 0:
                return None
            return str(element)

# def date_modifier(date_string: str) -> date:
#     date_list = date_string.split('/')
#     # noinspection PyUnusedLocal
#     date_format_key = ['int' for i in range(3)]
#     print('121:', 'date_format_key ''='' ', date_format_key)
#     finaldate = [FileReader.cast(date_format_key, date_list)
#                  for date_format_key, date_list in zip(date_format_key, date_list)]
#     assert all(isinstance(i, int) for i in finaldate)
#     date_object = date(finaldate[2], finaldate[0], finaldate[1])
#     # assert date_object.year == 2016
#     # assert date_object.month == 5
#     # assert date_object.day == 10
#     return date_object


# def infer_data_type(self):
#     for value in self.data_key:
#         if value is None:
#             self.data_key[self.data_key.index(value)] = None
#         elif all(c.isdigit() for c in value):
#             self.data_key[self.data_key.index(value)] = int(value)
#
#         elif value.count('.') == 1:
#             try:
#                 self.data_key[self.data_key.index(value)] = float(value)
#             except ValueError:
#                 self.data_key[self.data_key.index(value)] = str(value)
#
#         else:
#             self.data_key[self.data_key.index(value)] = str(value)


def parse_date(value, *, fmt='%Y-%m-%dT%H:%M:%SZ'):
    return datetime.strptime(value, fmt)
