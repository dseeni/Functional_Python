from src.parse_utils import *
from src.constants import *

# row = iter_file(fnames[0], 'personal_info', parsers[0])
# for rows in csv_reader(fnames[0]):
#     print(next(row))

# row_csv_extract(fnames[0], 3)
# rows_csv_extract(fnames, 3)
Personal_Info = create_named_tuple_class('Personal_Info', fnames[0])
print(zip_type_key(data_row_extract(fnames[0]), parsers[0]))
row = data_row_extract(fnames[0])
print(next(row))
# print(next(row))
# print(zip_type_key(row, parsers[0]))
# print(zip_type_key(row, parsers[0]))
# print(tuple(header_extract(fnames[0])))

