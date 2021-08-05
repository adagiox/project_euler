def naive_fib(i: int) -> int:
    if i == 1 or i == 2:
        return i
    return naive_fib(i-1) + naive_fib(i-2)


def fib(i: int) -> list[int]:
    # uses dynamic programming (aka a table to hold already calculated fib values)
    table = [1, 2]
    for i in range(2, i):
        table.append(table[-1] + table[-2])
    return table


def even_fib(table: list[int]) -> int:
    return sum(num for num in table if num % 2 == 0)


print(even_fib(fib(32)))
