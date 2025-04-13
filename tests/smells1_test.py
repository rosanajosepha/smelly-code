import pytest

from smells1 import calculate_total


def test_calculate_total_empty():
    assert calculate_total([]) == 0


def test_unknown_item():
    assert calculate_total(["kiwi"]) == 0


def test_total_no_discount():
    assert calculate_total(["apple", "banana", "cherry"]) == 2.25


def test_total_with_discount():
    assert calculate_total(["apple"] * 10) == 9
