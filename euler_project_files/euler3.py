"""
Time Complexity: O(sqrt(n))
Space Complexity: O(1)
"""


def largest_prime_factor(n):
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
        else:
            factor += 1
    return n


if __name__ == "__main__":
    number = 600851475143
    print(largest_prime_factor(number))
