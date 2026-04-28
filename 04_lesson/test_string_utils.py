import pytest
from string_utils import StringUtils

utils = StringUtils()


# Тесты capitalize
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("123", "123"),
    ("", ""),
    (" ", " ")
])
def test_capitalize_positive(input_str, expected):
    assert utils.capitalize(input_str) == expected


# Тесты trim
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("  whitespace  ", "whitespace  "),
    ("skypro", "skypro"),
    ("", ""),
    ("   ", "")
])
def test_trim_positive(input_str, expected):
    assert utils.trim(input_str) == expected


# Тесты contains
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("123", "2", True),
    ("", "a", False),
    ("SkyPro", "", True)
])
def test_contains_positive(string, symbol, expected):
    assert utils.contains(string, symbol) == expected


# Тесты delete_symbol
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("123", "2", "13"),
    ("aaa", "a", ""),
    ("SkyPro", "z", "SkyPro"),
    ("", "a", ""),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected


# Негативные сценарии
def test_none_input():
    with pytest.raises(AttributeError):
        utils.capitalize(None)
    with pytest.raises(AttributeError):
        utils.trim(None)


def test_delete_symbol_none():
    with pytest.raises(AttributeError):
        utils.delete_symbol(None, "a")
