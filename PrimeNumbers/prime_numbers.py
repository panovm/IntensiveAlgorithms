from typing import List


def prime_numbers(n: int) -> List[int]:
    """
    Return all prime numbers from 1 to n (including)

    Args:
        n (int): number

    Returns:
        List[int]: prime numbers
    """
    if n < 2:
        return 0
    deleted = set()
    prime = []
    for i in range(2, n+1):
        if i not in deleted:
            prime.append(i)
            j = 2
            while j * i <= n:
                deleted.add(j * i)
                j += 1
    return prime


# https://leetcode.com/problems/count-primes/
