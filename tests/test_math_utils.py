"""Comprehensive tests for math_utils module."""
import pytest
from src.math_utils import (
    add,
    clamp,
    divide,
    factorial,
    gcd,
    is_prime,
    lcm,
    multiply,
    subtract,
)


class TestAdd:
    def test_positive_numbers(self):
        assert add(2, 3) == 5

    def test_negative_numbers(self):
        assert add(-1, -4) == -5

    def test_mixed_signs(self):
        assert add(-3, 7) == 4

    def test_zero(self):
        assert add(0, 0) == 0
        assert add(5, 0) == 5
        assert add(0, 5) == 5

    def test_floats(self):
        assert add(1.5, 2.5) == 4.0

    def test_large_numbers(self):
        assert add(10**9, 10**9) == 2 * 10**9


class TestSubtract:
    def test_positive_result(self):
        assert subtract(10, 3) == 7

    def test_negative_result(self):
        assert subtract(3, 10) == -7

    def test_same_values(self):
        assert subtract(5, 5) == 0

    def test_zero(self):
        assert subtract(0, 0) == 0
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5

    def test_floats(self):
        assert subtract(3.5, 1.5) == pytest.approx(2.0)


class TestMultiply:
    def test_positive_numbers(self):
        assert multiply(3, 4) == 12

    def test_negative_numbers(self):
        assert multiply(-2, -3) == 6

    def test_mixed_signs(self):
        assert multiply(-2, 3) == -6

    def test_by_zero(self):
        assert multiply(100, 0) == 0
        assert multiply(0, 100) == 0

    def test_by_one(self):
        assert multiply(7, 1) == 7

    def test_floats(self):
        assert multiply(2.5, 4.0) == pytest.approx(10.0)


class TestDivide:
    def test_exact_division(self):
        assert divide(10, 2) == 5.0

    def test_non_exact_division(self):
        assert divide(7, 2) == pytest.approx(3.5)

    def test_negative_dividend(self):
        assert divide(-10, 2) == -5.0

    def test_negative_divisor(self):
        assert divide(10, -2) == -5.0

    def test_both_negative(self):
        assert divide(-10, -2) == 5.0

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)

    def test_zero_dividend(self):
        assert divide(0, 5) == 0.0


class TestFactorial:
    def test_zero(self):
        assert factorial(0) == 1

    def test_one(self):
        assert factorial(1) == 1

    def test_small_values(self):
        assert factorial(2) == 2
        assert factorial(3) == 6
        assert factorial(4) == 24
        assert factorial(5) == 120

    def test_larger_value(self):
        assert factorial(10) == 3628800

    def test_negative_raises(self):
        with pytest.raises(ValueError, match="non-negative"):
            factorial(-1)

    def test_non_integer_raises(self):
        with pytest.raises(TypeError, match="integer"):
            factorial(2.5)

    def test_non_integer_string_raises(self):
        with pytest.raises(TypeError):
            factorial("5")


class TestIsPrime:
    def test_less_than_two(self):
        assert is_prime(0) is False
        assert is_prime(1) is False
        assert is_prime(-5) is False

    def test_two_is_prime(self):
        assert is_prime(2) is True

    def test_three_is_prime(self):
        assert is_prime(3) is True

    def test_even_non_prime(self):
        assert is_prime(4) is False
        assert is_prime(100) is False

    def test_known_primes(self):
        for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
            assert is_prime(p) is True

    def test_known_non_primes(self):
        for n in [4, 6, 8, 9, 10, 12, 15, 25, 49]:
            assert is_prime(n) is False

    def test_large_prime(self):
        assert is_prime(997) is True

    def test_large_non_prime(self):
        assert is_prime(999) is False


class TestGcd:
    def test_basic(self):
        assert gcd(12, 8) == 4

    def test_one_is_zero(self):
        assert gcd(0, 5) == 5
        assert gcd(5, 0) == 5

    def test_both_zero(self):
        assert gcd(0, 0) == 0

    def test_same_values(self):
        assert gcd(7, 7) == 7

    def test_coprime(self):
        assert gcd(13, 17) == 1

    def test_negative_values(self):
        assert gcd(-12, 8) == 4
        assert gcd(12, -8) == 4
        assert gcd(-12, -8) == 4

    def test_one_divides_other(self):
        assert gcd(10, 5) == 5
        assert gcd(5, 10) == 5


class TestLcm:
    def test_basic(self):
        assert lcm(4, 6) == 12

    def test_zero(self):
        assert lcm(0, 5) == 0
        assert lcm(5, 0) == 0

    def test_same_values(self):
        assert lcm(7, 7) == 7

    def test_coprime(self):
        assert lcm(4, 9) == 36

    def test_one_is_multiple(self):
        assert lcm(3, 9) == 9

    def test_large_values(self):
        assert lcm(12, 18) == 36


class TestClamp:
    def test_within_range(self):
        assert clamp(5, 1, 10) == 5

    def test_below_min(self):
        assert clamp(-5, 0, 10) == 0

    def test_above_max(self):
        assert clamp(15, 0, 10) == 10

    def test_at_min(self):
        assert clamp(0, 0, 10) == 0

    def test_at_max(self):
        assert clamp(10, 0, 10) == 10

    def test_equal_min_max(self):
        assert clamp(5, 3, 3) == 3

    def test_invalid_range(self):
        with pytest.raises(ValueError, match="min_val"):
            clamp(5, 10, 0)

    def test_floats(self):
        assert clamp(1.5, 1.0, 2.0) == pytest.approx(1.5)
        assert clamp(0.5, 1.0, 2.0) == pytest.approx(1.0)
