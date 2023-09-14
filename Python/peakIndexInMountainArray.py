from typing import List


def peakIndexInMountainArray(arr: List[int]) -> int:
    idx = 0
    for i in range(len(arr-1)):
        if idx is not i and arr[idx] < arr[i]:
            idx = i
    return idx