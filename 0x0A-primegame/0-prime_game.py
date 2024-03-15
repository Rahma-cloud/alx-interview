#!/usr/bin/python3
""" Primegame Task """


def get_primes_up_to_n(n):
    """ gets the prime numbers """
    primes = []
    isPrime = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (isPrime[prime]):
            primes.append(prime)
            for j in range(prime, n + 1, prime):
                isPrime[j] = False
    return primes


def isWinner(x, nums):
    """ This function stores the winner """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for k in range(x):
        primes = get_primes_up_to_n(nums[k])
        if len(primes) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
