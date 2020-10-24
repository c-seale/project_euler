from math import sqrt


def is_prime(value: int) -> bool:
    val = abs(value)
    if val in [0, 1]:
        return False
    for potential_factor in range(2, int(sqrt(val)) + 1):
        if val % potential_factor == 0:
            return False
    return True
