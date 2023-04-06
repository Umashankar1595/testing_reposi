import pytest
import math


def factorial_function(number):
    assert number >= 0. and type(number) is int, "the input is not recognized"
    if number == 0:
        return 1
    else:
        return number * factorial_function(number - 1)


def test_factorial_functionality():
    print("inside test_factorial_functionality")
    assert factorial_function(0) == 1
    assert factorial_function(4) == 24


def test_standard_library():
    print("inside test_standard_library")
    for i in range(5):
        assert math.factorial(i) == factorial_function(i)


def test_negative_number():
    print("inside test_nagtive_number")
    with pytest.raises(AssertionError):
        factorial_function(-10)
