
'''
Check if array is sorted
Given an array arr[], check whether it is sorted in non-decreasing order. Return true if it is sorted otherwise false.

Examples:

Input: arr[] = [10, 20, 30, 40, 50]
Output: true
Explanation: The given array is sorted.
Input: arr[] = [90, 80, 100, 70, 40, 30]
Output: false
Explanation: The given array is not sorted.
Constraints:
1 ≤ arr.size ≤ 106
- 109 ≤ arr[i] ≤ 109
'''

class Solution:
    def isSorted(self, arr) -> bool:
        n = len(arr)
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                return False
        return True