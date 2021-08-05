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
