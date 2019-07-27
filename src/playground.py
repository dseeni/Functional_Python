from src.parse_utils import *
from src.constants import *
from itertools import starmap

# row = iter_file(fnames[0], 'personal_info', parsers[0])
# for rows in csv_reader(fnames[0]):
#     print(next(row))

# row_csv_extract(fnames[0], 3)
# rows_csv_extract(fnames, 3)
Personal_Info = create_named_tuple_class('Personal_Info', fnames[0])
row = data_row_extract(fnames[0])
zipped_row = zip_type_key(next(row), parsers[0])
# print(next(row))
# print(zip_type_key(next(row), parsers[0]))
# print(zip_type_key(next(row), parsers[0]))
# print(zip_type_key(row, parsers[0]))
# print(zip_type_key(row, parsers[0]))
# print(tuple(header_extract(fnames[0])))

# print(zipped_row)
# print(cast_zipped_row(zipped_row))

# print(list(iter_file(fnames[0], 'Personal_Info', parsers[0])))
# print(len(list(iter_file(fnames[0], 'Personal_Info', parsers[0]))))
# assert list(parsers[0]) == list(type(i) for i in cast_zipped_row(zipped_row))

for filename, class_name, parser in zip(fnames, class_names, parsers):
    file_iter = iter_file(filename, class_name, parser)
    print(filename)
    for _ in range(10):
        print(next(file_iter))
    print()
