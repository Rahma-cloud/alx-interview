#!/usr/bin/python3
""" Primegame Task """

def isWinner(x, nums):
    """ This function stores the winner """
    def is_prime(num):
        """ This function checks if a number is a prime number """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes_cache = {}

    def get_primes_up_to_n(n):
        """ Get primes up to n using memoization """
        if n in primes_cache:
            return primes_cache[n]
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        primes_cache[n] = primes
        return primes

    winners = []

    for n in nums:
        primes = get_primes_up_to_n(n)
        count = sum(1 for prime in primes if prime <= n)
        winner = "Maria" if count % 2 != 0 else "Ben"
        winners.append(winner)

    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
