
'''
Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Return the indices (1-based) of the two numbers.

Input: numbers = [2, 7, 11, 15], target = 9
Output: [1, 2]
Constraints: Must use only constant extra space.
'''

from typing import List

def two_sum(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
        
    return []   # if no solution is found