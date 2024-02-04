import pytest

from myapp.app import multiply_by_two, divide_by_two

class maths:
    def add(a, b):
        return a + b


    def subtract(a, b):
        return a - b


    def multiply(a, b):
        return a * b


    def divide(a, b):
        return a * 1.0 / b

@pytest.fixture
def numbers():
    a = 10
    b = 20
    return [a,b]


class TestApp:
    def test_multiplication(self, numbers):
        res = multiply_by_two(numbers[0])
        assert res == numbers[1]

    def test_division(self, numbers):
        res = divide_by_two(numbers[1])
        assert res == numbers[0]
