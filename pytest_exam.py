import pytest
def increment(x):
    return x + 1
def test_answer():
    assert increment(9) == 10
