def summation_of_primes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    return sum(i for i, is_prime in enumerate(sieve) if is_prime)
print(summation_of_primes(2000000))