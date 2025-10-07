"""
Time Complexity: O(10^{2n}), where n is the number of digits
Space Complexity: O(1)
"""


def largest_palindrome_product(n):
    """Find the largest palindrome made from the product of two n-digit numbers."""
    if n < 1:
        return None

    upper_limit = 10**n - 1
    lower_limit = 10**(n - 1)

    max_palindrome = 0

    for i in range(upper_limit, lower_limit - 1, -1):
        for j in range(i, lower_limit - 1, -1):
            product = i * j
            if product <= max_palindrome:
                break
            if str(product) == str(product)[::-1]:
                max_palindrome = product

    return max_palindrome


print(largest_palindrome_product(3))
