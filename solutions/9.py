"""
    Project Euler: Special Pythagorean triplet (Problem 9)
    https://projecteuler.net/problem=9

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
"""

TARGET_SUM = 1000


def find_triplet(target_sum):
    for c in range(1, target_sum):
        for b in range(1, target_sum):
            if b > c:
                break
            for a in range(1, target_sum):
                if a > b or a > c:
                    break
                if a + b + c == target_sum and a ** 2 + b ** 2 == c ** 2:
                    return a, b, c


triple = find_triplet(TARGET_SUM)
print(f'Product abc: {triple[0]}*{triple[1]}*{triple[2]}={triple[0] * triple[1] * triple[2]}')
