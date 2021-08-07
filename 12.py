from helpers import factors
from typing import Iterator


def next_in_series() -> Iterator[int]:
    i = 1
    while True:
        yield i
        i += 1


def next_triangle_number() -> Iterator[int]:
    s = 0
    for i in next_in_series():
        s += i
        yield s


def highly_divisible_triangle() -> int:
    triangles = next_triangle_number()
    for num in triangles:
        if len(factors(num)) > 500:
            return num
    return 0


print(highly_divisible_triangle())
