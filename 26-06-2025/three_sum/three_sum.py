'''
3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i ≠ j ≠ k and nums[i] + nums[j] + nums[k] == 0.
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
'''

from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:

    nums.sort()
    result = []
    n = len(nums)

    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left = i+1
        right = n-1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left = left + 1
                right = right - 1

                while left < right and nums[left] == nums[left - 1]:
                    left = left + 1
                while left < right and nums[right] == nums[right + 1]:
                    right = right - 1

            elif total < 0:
                left = left + 1
            else:
                right = right - 1

    return result
