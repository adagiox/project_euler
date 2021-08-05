from helpers import *


def test_is_prime():
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(7) == True
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False
    assert is_prime(11) == True


def test_is_multiple():
    assert is_multiple(4, 4) == True
    assert is_multiple(4, 2) == True
    assert is_multiple(4, 3) == False
    assert is_multiple(4, 5) == False
    assert is_multiple(4, 0) == False


def test_prime_factors():
    assert prime_factors(13195) == [5, 7, 13, 29]
    assert prime_factors(600851475143) == [71, 839, 1471, 6857]


def test_is_palindrome():
    assert is_palindrome(9009) == True
    assert is_palindrome(9) == True
    assert is_palindrome(909) == True
    assert is_palindrome(123) == False
    assert is_palindrome(223) == False


def test_is_pythagorean_triplet():
    assert is_pythagorean_triplet(3, 4, 5) == True
    assert is_pythagorean_triplet(4, 4, 4) == False
