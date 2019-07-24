from src.parse_utils import *
from src.constants import *


def test_pass_default():
    pass
    # assert parse_date() == 'This is a passed test man'


def test_header_extract():
    headers = list(header_extract(fnames))
    print(headers)
    assert len(headers) == 4
    assert headers[0][0] == 'ssn'

