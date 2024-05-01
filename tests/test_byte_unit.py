import unittest

import pytest

from byte_unit.byte_unit import ByteUnit, parse_byte_string, to_bytes, convert_to_unit


class TestByteUnit(unittest.TestCase):

    def test_byte_unit_suffixes(self):
        assert sorted(["b", "k", "kb", "m", "mb", "g", "gb"]) == sorted(ByteUnit.get_all_suffixes())

    def test_get_byte_unit_from_suffix(self):
        assert ByteUnit.GB == ByteUnit.get_byte_unit_from_suffix("g")
        assert ByteUnit.MB == ByteUnit.get_byte_unit_from_suffix("MB")


def test_parse_byte_string():
    actual_value, actual_unit = parse_byte_string("1K")

    assert actual_value == "1"
    assert actual_unit == ByteUnit.KB


def test_parse_byte_string_should_raise_error_for_unsupported_suffix():
    with pytest.raises(ValueError):
        parse_byte_string("1x")


def test_conversion_to_bytes():
    assert to_bytes(1024) == 1024
    assert to_bytes("2KB") == 2048


def test_convert_to_unit():
    assert convert_to_unit("1024m", ByteUnit.GB) == 1


def test_convert_to_unit_should_consider_it_as_bytes_when_no_suffix_is_in_string():
    assert convert_to_unit("1024", ByteUnit.KB) == 1


def test_convert_to_unit_from_higher_to_lower_grain():
    assert convert_to_unit("1g", ByteUnit.MB) == 1024


if __name__ == '__main__':
    unittest.main()
