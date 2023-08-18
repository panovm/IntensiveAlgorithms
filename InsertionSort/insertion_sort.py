from typing import List


def insertion_sort(array: List[int]) -> List[int]:
    """
    Sorts the array in ascending order using insertion sort

    Args:
        array (List[int]): input

    Returns:
        List[int]: sorted array
    """

    for i in range(len(array)):
        for j in range(i-1, -1, -1):
            if array[j+1] < array[j]:
                array[j + 1], array[j] = array[j], array[j + 1]
    return array


# https://leetcode.com/problems/sort-colors/
