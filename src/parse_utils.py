from itertools import islice
from src.constants import fnames, parsers, class_names
from csv import reader
from datetime import date
from src.constants import *

# read file as csv
def read_file(file_name):
    with open(file_name) as f:
        rows = reader(f, delimiter=',', quotechar='"')
        yield from rows

def header_extract(file_names):
    for file in file_names:
        with open(file) as f:
            header = reader(f, delimiter=',', quotechar='"')
            return header
    # with open(self.filename) as file:
    #     next(file)
    #     data_string = next(file).strip('\n')
    #     self.data_key = data_string.split(',')
    #     self.infer_data_type()

# read N lines for file in fnames
for file in src.constants.fnames:
    lines = read_file(file)
    for line in islice(lines, 5):
        print(line)


def cast(single_data_value, data_value):
    if single_data_value is None:
        return None
    elif single_data_value == 'float':
        return float(data_value)
    elif single_data_value == 'int':
        return int(data_value)
    else:
        if len(str(data_value)) is 0:
            return None
        return str(data_value)

def date_modifier(date_string: str) -> date:
    date_list = date_string.split('/')
    # noinspection PyUnusedLocal
    date_format_key = ['int' for i in range(3)]
    print('121:', 'date_format_key ''='' ', date_format_key)
    finaldate = [FileReader.cast(date_format_key, date_list)
                 for date_format_key, date_list in zip(date_format_key, date_list)]
    assert all(isinstance(i, int) for i in finaldate)
    date_object = date(finaldate[2], finaldate[0], finaldate[1])
    # assert date_object.year == 2016
    # assert date_object.month == 5
    # assert date_object.day == 10
    return date_object




def infer_data_type(self):
    for value in self.data_key:
        if value is None:
            self.data_key[self.data_key.index(value)] = None
        elif all(c.isdigit() for c in value):
            self.data_key[self.data_key.index(value)] = int(value)

        elif value.count('.') == 1:
            try:
                self.data_key[self.data_key.index(value)] = float(value)
            except ValueError:
                self.data_key[self.data_key.index(value)] = str(value)

        else:
            self.data_key[self.data_key.index(value)] = str(value)

def parse_date():
    return 'temp_date'
