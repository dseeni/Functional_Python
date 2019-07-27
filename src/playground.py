from src.parse_utils import *
from src.constants import *
from itertools import starmap, chain

# iter_files(fnames, class_names, parsers, 10)

# -------------- Goal_2 --------------
# chained 4 data rows from raw extract
# chained headers from raw header extract
# chained truth values of parsers compressed
# compress chained headers
# create named tuple based on chained compressed chained header
# compressed raw chained data rows with chained parser compress
# return named combined tuple with combined row


row = next(iter_combined_files_data_row(fnames, class_names, parsers, compress_fields))


# print(*list(iter_combined_files(fnames, class_names, parsers, compress_fields)), sep='\n')
# print(len(list(iter_combined_files(fnames, class_names, parsers, compress_fields))))


# -------------- Goal_3 --------------
stale_records = list(filter_iter_combined(fnames, class_names, parsers, compress_fields,
                                          key=lambda row: row.last_updated < cut_off_date))

print(*list(filter_iter_combined(fnames, class_names, parsers, compress_fields,
                                 key=lambda row: row.last_updated < cut_off_date)), sep='\n')

# -------------- Goal_4 --------------

