from sys import maxsize

from funcs.math import is_prime

"""
    Project Euler: 10001st prime (Problem 7)
    https://projecteuler.net/problem=7


    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10 001st prime number?
"""

TARGET_PRIME_INDEX = 10001


def get_prime_by_index(target_index: int) -> int:
    primes = []
    for i in range(1, maxsize):
        if len(primes) == target_index:
            return primes[-1]
        if is_prime(i):
            primes.append(i)


print(get_prime_by_index(TARGET_PRIME_INDEX))
