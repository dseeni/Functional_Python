from src.parse_utils import *
from src.constants import *
from itertools import starmap, chain

# print([next(i) for i in rows])
iter_files(fnames, class_names, parsers, 10)

