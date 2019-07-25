from src.parse_utils import *
from src.constants import *

row = iter_file(fnames[0], 'personal_info', parsers[0])
for rows in csv_reader(fnames[0]):
    print(next(row))


