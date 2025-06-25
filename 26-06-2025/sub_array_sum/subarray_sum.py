
'''
Subarray Sum Equals K
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
Input: l1 = [1,1,1], k = 2
Output: 2
'''

from typing import List

def subarray_sum(l1: List[int], k: int) -> int:
    count = 0
    current_sum = 0
    prefix_sums = {0: 1}

    for num in l1:
        current_sum = current_sum + num
        difference = current_sum - k

        if difference in prefix_sums:
            count = count + prefix_sums[difference]

        if current_sum in prefix_sums:
            prefix_sums[current_sum] = prefix_sums[current_sum] + 1
        else:
            prefix_sums[current_sum] = 1

    return count