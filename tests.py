import print_table as print_table
import pytest


def test_sum():
    assert print_table.sum(1,2)==3
    assert print_table.sum(1,4)==5
    


@pytest.mark.parametrize("input_value, expected_result", [
    (2, True),
    (3, False),
    ([], TypeError),
    ({}, TypeError),
    ("asdsd", TypeError),
])


def test_is_even(input_value, expected_result):
    if isinstance(expected_result, type):
        with pytest.raises(expected_result):
            print_table.is_even(input_value)
    else:
        assert print_table.is_even(input_value) == expected_result

def test_return_katinha():
    assert print_table.return_katinha()=="linda"
