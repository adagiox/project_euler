from helpers import is_prime


def nth_prime(n: int) -> int:
    primes = 0
    num = 2
    last_prime = 2
    while primes < n:
        if is_prime(num):
            primes += 1
            last_prime = num
        num += 1
    return last_prime


print(nth_prime(10_001))
