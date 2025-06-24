
'''
Given an array nums, return the element that appears more than ⌊n / 2⌋ times.
Input: nums = [3,2,3]
Output: 3
'''
from typing import List

def majority_element(nums: List[int]) -> int:
    count = 0
    major = None

    for num in nums:
        if count == 0:
            major = num
        
        if num == major:
            count = count + 1
        else:
            count = count - 1

    return major