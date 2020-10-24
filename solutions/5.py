from sys import maxsize

"""
    Project Euler: Smallest multiple (Problem 5)
    https://projecteuler.net/problem=5

    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

DIVISIBLE_RANGE = (1, 20)
MAX_SEARCH = maxsize

for i in range(1, MAX_SEARCH + 1):
    divisible = True
    for divider in range(DIVISIBLE_RANGE[0], DIVISIBLE_RANGE[1] + 1):
        if i % divider != 0:
            divisible = False
            break

    if divisible:
        print(i)
        break
