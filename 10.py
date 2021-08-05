from math import sqrt
from helpers import is_prime


def summation_of_primes(max_range: int) -> int:
    sum_of_primes = 0
    primes = [True for i in range(max_range)]
    i = 2
    limit = sqrt(max_range)
    while i < limit:
        n = 2
        while (n * i) < max_range:
            primes[n*i] = False
            n += 1
        for index, p in enumerate(primes[i+1:]):
            if p == True:
                i = i + index + 1
                break
        print(i)
    for index, p in enumerate(primes):
        if p == True:
            sum_of_primes += index
    return sum_of_primes - 1


print(summation_of_primes(2_000_000))
