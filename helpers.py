from math import sqrt
from typing import Iterator


def is_multiple(num: int, multiple: int) -> bool:
    if multiple == 0:
        return False
    return num % multiple == 0


def is_prime(num: int) -> bool:
    if num <= 1 or num == 4:
        return False
    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True


def factors(num: int) -> list[int]:
    factor_set = {}
    for divisor in range(1, int(sqrt(num)) + 1):
        if num % divisor == 0:
            factor_set[divisor] = 1
            factor_set[num // divisor] = 1
    return list(factor_set.keys())


def prime_factors(num: int) -> list[int]:
    factors = []
    current = 2
    while num > 1:
        if is_prime(current) and num % current == 0:
            factors.append(current)
        while num % current == 0:
            num //= current
        current += 1
    return factors


def is_palindrome(num: int) -> bool:
    return list(str(num)) == list(str(num))[::-1]


def is_pythagorean_triplet(a: int, b: int, c: int) -> bool:
    return a < b < c and (a*a + b*b) == c*c


def next_collatz(num: int) -> Iterator[int]:
    yield num
    while num > 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = 3*num + 1
        yield num


def collatz_sequence(num: int) -> list[int]:
    return [n for n in next_collatz(num)]

