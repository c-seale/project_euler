from typing import List, Optional

"""
    Project Euler: Even Fibonacci numbers (Problem 2)
    https://projecteuler.net/problem=2


    Each new term in the Fibonacci sequence is generated by adding the previous two terms.
    By starting with 1 and 2, the first 10 terms will be:

        1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do not exceed four million,
    find the sum of the even-valued terms.
"""

MAX_FIBONACCI_VALUE = 4000000


def calc_fib_list(max_value: int, running_list: Optional[List] = None) -> List[int]:
    """
    Generate a list containing the fibonacci number sequence values. The last value in the list may not exceed max_value
    :param max_value: Fibonacci numbers may not exceed this value
    :param running_list: List of currently calculated Fibonacci numbers
    :return: List of fibonacci numbers
    """
    if running_list is None:
        running_list = [1, 2]

    new_fib = running_list[-1] + running_list[-2]
    if new_fib >= max_value:
        return running_list

    running_list.append(new_fib)
    return calc_fib_list(max_value, running_list)


running_sum = 0
for fib in calc_fib_list(MAX_FIBONACCI_VALUE):
    if fib % 2 == 0:
        running_sum += fib

print(f'Total sum of all even Fibonacci numbers lower than {MAX_FIBONACCI_VALUE}: {running_sum}')
