import pytest
from app.calculator import add, subtract, multiply, divide, is_prime


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2


def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(5, 0) == 0


def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5


def test_divide_by_zero_raises():
    with pytest.raises(ValueError):
        divide(1, 0)


@pytest.mark.parametrize("n,expected", [
    (0, False), (1, False), (2, True), (3, True),
    (4, False), (17, True), (18, False), (97, True),
])
def test_is_prime(n, expected):
    assert is_prime(n) is expected


def test_is_prime_type_error():
    with pytest.raises(TypeError):
        is_prime("7")
