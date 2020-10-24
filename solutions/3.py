from math import sqrt
from typing import List

"""
    Project Euler: Largest prime factor (Problem 3)
    https://projecteuler.net/problem=3


    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
"""

TARGET = 600851475143


def is_prime(value: int) -> bool:
    val = abs(value)
    if val in [0, 1]:
        return False
    for potential_factor in range(2, int(sqrt(val)) + 1):
        if val % potential_factor == 0:
            return False
    return True


def get_prime_factors(value: int) -> List[int]:
    prime_factors = []
    for potential_factor in range(1, int(sqrt(value)) + 1):
        if value % potential_factor == 0 and is_prime(potential_factor):
            prime_factors.append(potential_factor)
    return sorted(prime_factors)


print(f'Largest prime factor of {TARGET} is {get_prime_factors(TARGET)[-1]}')
