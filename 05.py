def smallest_multiple() -> int:
    num = 20
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    while True:
        for i in nums:
            if num % i != 0:
                break
        else:
            return num
        num += 1


print(smallest_multiple())
