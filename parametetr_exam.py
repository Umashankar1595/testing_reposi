import pytest
def is_odd(number):
    return number % 2 !=0
@pytest.mark.parametrize('odd', range(1, 11, 2))
@pytest.mark.parametrize('even', range(0, 10, 2))
def test_sum_odd_even_returns_odd(odd, even):
    assert is_odd(odd + even)

@pytest.fixture(params=range(1, 11, 2))
def odd(request):
    return request