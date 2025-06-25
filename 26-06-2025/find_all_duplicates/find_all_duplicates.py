
'''
Find All Duplicates in an Array
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others once. Return all the elements that appear twice.
Input: L1 = [4,3,2,7,8,2,3,1]
Output: [2,3]
'''

from typing import List

def find_duplicates(L1: List[int]) -> List[int]:

    result = []

    for num in L1:
        index = abs(num) - 1

        if L1[index] < 0:
            result.append(abs(num))
        else:
            L1[index] = -L1[index]

    return result