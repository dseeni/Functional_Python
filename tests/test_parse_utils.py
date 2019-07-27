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


def test_zip_type_key():
    key = zip_type_key(next(data_row_extract(fnames[0])), parsers[0])
    assert type(key[0][0]) == key[0][1]


def test_cast_zipped_row():
    castedrow = cast_zipped_row(zip_type_key(next(data_row_extract(fnames[0])), parsers[0]))
    assert type(castedrow[0]) == str


def test_parse_date():
    date = '2017-10-07T00:14:42Z'
    formatted_date = parse_date(date)
    assert formatted_date.day == 7
    assert formatted_date.year == 2017
    assert formatted_date.month == 10


def test_iter_file():
    row = data_row_extract(fnames[0])
    zipped_row = zip_type_key(next(row), parsers[0])
    file_rows = iter_file(fnames[0], 'Personal_Info', parsers[0])
    nextrow = next(file_rows)
    assert nextrow.ssn == '100-53-9824'
    assert (len(list(iter_file(fnames[0], 'Personal_Info', parsers[0])))) == 1000
    assert list(parsers[0]) == list(type(i) for i in cast_zipped_row(zipped_row))


def test_iter_files():
    iter_files(fnames, class_names, parsers, 10)


def test_create_combined_named_tuple_class():
    row_tuple = create_combined_named_tuple_class(fnames, compress_fields)
    datarow = row_tuple(*next(iter_combined_files_data_row(fnames, class_names, parsers, compress_fields)))
    assert len(datarow) == 13
    assert datarow.ssn == '100-53-9824'


def test_iter_combined_files():
    datarow = next(iter_combined_files(fnames, class_names, parsers, compress_fields))
    assert len(datarow) == 13
    assert datarow.ssn == '100-53-9824'


def test_filter_iter_combined():
    stale_records = list(filter_iter_combined(fnames, class_names, parsers, compress_fields,
                                              key=lambda x: x.last_updated < cut_off_date))
    assert len(stale_records) == 129
