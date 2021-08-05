from helpers import is_prime


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


def largest_prime_factor(num: int) -> int:
    return prime_factors(num)[-1]


print(largest_prime_factor(600851475143))
