
'''
Given an array, rotate the array to the right by k steps, where k is non-negative.
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
'''
from typing import List

def rotate_array(nums: List[int], k: int) -> List[int]:

    n = len(nums)

    if n == 0:
        return []
    
    k = k % n

    rotated = nums[-k:] + nums[:-k]

    return rotated