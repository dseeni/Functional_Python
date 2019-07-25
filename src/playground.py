from src.parse_utils import *
from src.constants import *
import os
from itertools import chain
from collections import namedtuple

headers = list(header_extract(fnames))
print(headers)
# print(len(headers))
# print(list(data_row_extract(fnames)))
final_rows_data_types = [list(zip(list(data_row_extract(fnames))[i], parsers[i])) for i in range(len(parsers))]
print(final_rows_data_types)

data = [cast(i[0], i[1]) for i in final_rows_data_types for j in i]
# print(final_rows_data_types)
# print(data)

# namedtuples =  [namedtuple('final_data_row', header) for header in headers]
# for i in range(len(final_rows)):
#     finalnamed = namedtuples[i]
#     finalrownamed = finalnamed(*final_rows[i])
#     print(*finalrownamed, sep='\n')




