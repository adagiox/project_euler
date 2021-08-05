from helpers import is_palindrome


from helpers import is_palindrome


def largest_palindrome_product() -> int:
    palindromes = []
    for i in range(100, 999):
        for j in range(100, 999):
            k = i * j
            if is_palindrome(k):
                palindromes.append(k)
    return max(palindromes)


print(largest_palindrome_product())
