from helpers import collatz_sequence


def longest_collatz_sequence(upper_limit: int) -> int:
    sequence_length = {}
    for i in range(upper_limit):
        sequence_length[i] = len(collatz_sequence(i))
    return max(sequence_length, key=lambda x: sequence_length[x])


print(longest_collatz_sequence(1_000_000))
