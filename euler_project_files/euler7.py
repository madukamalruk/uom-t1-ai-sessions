"""
Time Complexity: O(n*sqrt(n)), where n is the number of primes to find
Space Complexity: O(1)
"""


def prime_10001st():
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

    What is the 10 001st prime number?
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    num = 1
    while count < 10001:
        num += 1
        if is_prime(num):
            count += 1
    return num


print(prime_10001st())
