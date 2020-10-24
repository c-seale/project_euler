"""
    Project Euler: Sum square difference (Problem 6)
    https://projecteuler.net/problem=6


    Find the difference between the sum of the squares of the first one hundred natural
    numbers and the square of the sum.
"""

TARGET_RANGE = (1, 100)

sum_of_squares = 0
for i in range(TARGET_RANGE[0], TARGET_RANGE[1] + 1):
    sum_of_squares += i ** 2

# Generalized Gauss summation formula
square_of_the_sum = ((TARGET_RANGE[0] + TARGET_RANGE[1]) * (TARGET_RANGE[1] - TARGET_RANGE[0] + 1) // 2) ** 2

print(f'Sum of the squares in range ({TARGET_RANGE[0], TARGET_RANGE[1]}): {sum_of_squares}')
print(f'Square of the sum of numbers in range ({TARGET_RANGE[0], TARGET_RANGE[1]}): {square_of_the_sum}')
print(f'Difference between sum of squares and the square of the sum: {abs(sum_of_squares - square_of_the_sum)}')
