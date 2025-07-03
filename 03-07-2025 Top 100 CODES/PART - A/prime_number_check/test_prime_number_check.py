
import pytest
from prime_number_check import Solution  

s = Solution()

def test_prime_numbers():
    assert s.isPrime(2) is True
    assert s.isPrime(3) is True
    assert s.isPrime(5) is True
    assert s.isPrime(17) is True
    assert s.isPrime(97) is True
    assert s.isPrime(9973) is True

def test_non_prime_numbers():
    assert s.isPrime(1) is False
    assert s.isPrime(0) is False
    assert s.isPrime(-7) is False
    assert s.isPrime(4) is False
    assert s.isPrime(100) is False

def test_type_errors():
    with pytest.raises(TypeError):
        s.isPrime("11")
    with pytest.raises(TypeError):
        s.isPrime(7.0)
    with pytest.raises(TypeError):
        s.isPrime(None)
