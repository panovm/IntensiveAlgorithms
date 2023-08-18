from typing import List


def selection_sort(array: List[int]) -> List[int]:
    """
    Sorts the array in ascending order using selection sort

    Args:
        array (List[int]): input

    Returns:
        List[int]: sorted array
    """

    for i in range(len(array) - 1):
        a_min = array[i]
        for j in range(i, len(array)):
            if array[j] < a_min:
                a_min = array[j]
        array[i] = a_min
    return array


# https://leetcode.com/problems/sort-colors/
