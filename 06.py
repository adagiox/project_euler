def sum_square_difference() -> int:
    return sum(i for i in range(101))**2 - sum(i**2 for i in range(101))


print(sum_square_difference())
