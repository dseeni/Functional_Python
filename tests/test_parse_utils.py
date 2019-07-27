from src.parse_utils import *
from src.constants import *


def test_pass_default():
    pass
    # assert parse_date() == 'This is a passed test man'


def test_header_extract():
    headers = list(header_extract(fnames[0]))
    print(headers)
    assert len(headers) == 5
    assert headers[0] == 'ssn'


def test_row_csv_extract():
    rows = list(row_csv_extract(fnames[0], 5))
    assert len(rows) == 5
    assert rows[0][0] == 'ssn'


def test_rows_csv_extract():
    files_rows = list(rows_csv_extract(fnames, 5))
    assert len(files_rows[0]) == 5
    assert files_rows[0][0] == 'ssn'


def test_data_row_extract():
    data_row = next(data_row_extract(fnames[0]))
    assert len(data_row) == 5
    assert data_row[0] == '100-53-9824'


def test_create_named_tuple_class():
    personal_info = create_named_tuple_class('Personal_Info', fnames[0])
    info = personal_info(*next(data_row_extract(fnames[0])))
    print(info.ssn)
    assert info.ssn == '100-53-9824'
