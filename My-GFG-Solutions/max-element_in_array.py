
'''
Maximum Element in Array

Given an array arr[]. The task is to find the largest element and return it.

Examples:
Input: arr = [1, 8, 7, 56, 90]
Output: 90
Explanation: The largest element of the given array is 90.
Input: arr = [5, 5, 5, 5]
Output: 5
Explanation: The largest element of the given array is 5.
Input: arr = [10]
Output: 10
Explanation: There is only one element which is the largest.

Constraints:
1 <= arr.size()<= 10^6
0 <= arr[i] <= 10^6
'''


from typing import List
import array

class Solution:
    def largest(self, arr : List[int]) -> int:
        arr_new = array.array('i', arr)
        
        max_val = arr_new[0]
        
        for num in arr_new:
            if num > max_val:
                max_val = num
        return max_val