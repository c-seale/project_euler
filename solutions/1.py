"""
    Project Euler: Multiples of 3 and 5 (Problem 1)


    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
"""

RANGE_MIN = 1
RANGE_MAX = 1000
MULTIPLES = [3, 5, 6, 9]

running_sum = 0
for i in range(RANGE_MIN, RANGE_MAX):
    for multiple in MULTIPLES:
        if i % multiple == 0:
            running_sum += i
            break

print(f'Total sum of all multiples of {MULTIPLES} in RANGE({RANGE_MIN}, {RANGE_MAX}): {running_sum}')
