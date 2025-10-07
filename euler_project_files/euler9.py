"""
Time Complexity: O(n^2), where n = 1000
Space Complexity: O(1)
"""


def special_pythagorean_triplet():
    for a in range(1, 1000):
        for b in range(a, 1000 - a):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                return a * b * c


print(special_pythagorean_triplet())
