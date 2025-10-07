"""
Time Complexity: O(n)
Space Complexity: O(1)
"""


def sum_square_difference(n):
    sum_of_squares = sum(i**2 for i in range(1, n + 1))
    square_of_sum = sum(range(1, n + 1)) ** 2
    return square_of_sum - sum_of_squares


print(sum_square_difference(100))
