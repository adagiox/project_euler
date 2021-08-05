from helpers import is_pythagorean_triplet


def special_pythagorean_triplet() -> int:
    for a in range(1000):
        for b in range(a, 1000):
            for c in range(b, 1000):
                if a + b + c == 1000 and is_pythagorean_triplet(a, b, c):
                    return a*b*c


print(special_pythagorean_triplet())
