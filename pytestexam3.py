import pytest
def test_zero_divsion():
    with pytest.raises(ZeroDivisionError):
        4/1