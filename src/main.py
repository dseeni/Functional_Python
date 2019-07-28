from src.constants import *
from src.parse_utils import *

for gender in ('Female', 'Male'):
    results = group_data(fnames, class_names, parsers, compress_fields,
                         filter_key_composite(cut_off_date, gender), lambda row: row.vehicle_make)
    print(f'***************{gender}****************')
    print(list(results))
