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

    def get_primes_up_to_n(n):
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def calculate_winner(primes, n):
        """ Count the number of primes less than or equal to n """
        count = sum(1 for prime in primes if prime <= n)
        return "Maria" if count % 2 != 0 else "Ben"

    winners = []

    for round_num in range(x):
        n = nums[round_num]
        primes = get_primes_up_to_n(n)
        winner = calculate_winner(primes, n)
        winners.append(winner)

    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
