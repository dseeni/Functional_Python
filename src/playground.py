from src.parse_utils import *
from src.constants import *
from itertools import starmap, chain

# row = iter_file(fnames[0], 'personal_info', parsers[0])
# for rows in csv_reader(fnames[0]):
#     print(next(row))

# row_csv_extract(fnames[0], 3)
# rows_csv_extract(fnames, 3)
# Personal_Info = create_named_tuple_class('Personal_Info', fnames[0])
# row = data_row_extract(fnames[0])
# zipped_row = zip_type_key(next(row), parsers[0])
# print(next(row))
# print(zip_type_key(next(row), parsers[0]))
# print(zip_type_key(next(row), parsers[0]))
# print(zip_type_key(row, parsers[0]))
# print(zip_type_key(row, parsers[0]))
# print(tuple(header_extract(fnames[0])))

# zipped_row = zip_type_key(next(row), parsers[0])
# print(zipped_row)
# print(cast_zipped_row(zipped_row))
# print(list(iter_file(fnames[0], 'Personal_Info', parsers[0])))
# print(len(list(iter_file(fnames[0], 'Personal_Info', parsers[0]))))
# assert list(parsers[0]) == list(type(i) for i in cast_zipped_row(zipped_row))

# datarow = data_row_extract(fnames[0])
# rows = combined_data_row_extract(fnames)
# print(list(rows))
# print(list(flatten_combined_data_rows(next(rows))))
# flat = flatten_combined_data_rows(rows)
# print(list(rows))
# print(list(next(rows)))
# print(list(rows))
# print(list(next(rows)))
# print(list(rows))
# for i in rows:
#     print(next(i))

# print([next(i) for i in rows])
iter_files(fnames, class_names, parsers, 10)

