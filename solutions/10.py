from funcs.math import is_prime

"""
    Project Euler: Summation of primes (Problem 10)
    https://projecteuler.net/problem=10

    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
"""

MAX_PRIME = 2000000

running_sum = 0
for i in range(1, MAX_PRIME + 1):
    if is_prime(i):
        running_sum += i

print(f'The sum of all primes below {MAX_PRIME} is {running_sum}')
