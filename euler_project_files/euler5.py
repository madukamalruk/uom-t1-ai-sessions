def smallest_multiple(n):
    """Finds the smallest positive number that is evenly divisible by all of the numbers from 1 to n."""
    from math import gcd
    from functools import reduce

    def lcm(a, b):
        return a * b // gcd(a, b)

    return reduce(lcm, range(1, n + 1))

print(smallest_multiple(20))    