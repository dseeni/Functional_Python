from src.parse_utils import *
from src.constants import *
import os
from itertools import chain
# print(read_file_rows(fnames, 5))
fnames = fpersonal, femployment, fvehicles, fupdate_status
# print(*list(header_extract(fnames)), sep='\n')

# print each data row per file
# print(*list(data_row_extract(fnames)), sep='\n')
# print('====')
# print(*list(parsers), sep='\n')
# for i in range(len(parsers)):
#     print(parsers[i])
fl = []
for i in range(len(parsers)):
    fl.append(list(zip(list(data_row_extract(fnames))[i], parsers[i])))
# print(*fl, sep='\n')
# for i in fl:
#     data.append(cast(i[0], i[1]))
# print([cast(j[0], j[1]) for j in i for i in fl])
# print(data)
# for i in fl:
#     for j in i:
#         data.append(cast(j[0], j[1]))

data = [cast(j[0], j[1]) for i in fl for j in i]


print(data)
# print(len(data))
keys = list(chain(*parsers))
# print(keys)
datatypes = [type(i) for i in data]
print(datatypes)
# assert datatypes == keys
# print(datatypes, keys)

# print(len(list(parsers)))
# print(list(parsers))

# cast each data row per file per data key


