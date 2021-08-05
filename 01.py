from helpers import is_multiple

if __name__ == "__main__":
    nums = []
    for i in range(3, 1000):
        if is_multiple(i, 3) or is_multiple(i, 5):
            nums.append(i)
    print(sum(nums))

