from src.parse_utils import parse_date


def test_pass_default():
    assert parse_date() == 'This is a passed test man'
