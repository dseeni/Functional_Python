from src.parse_utils import *
from src.constants import *

# print(read_file_rows(fnames, 5))

# fnames = fpersonal, femployment, fvehicles, fupdate_status
print(*list(header_extract(fnames)), sep='\n')


