
'''
Perfect Array

Given an array arr[] of non-negative integers, determine whether the array is perfect. An array is considered perfect if it first strictly increases, then remains constant, and finally strictly decreases. Any of these three parts can be empty.

Examples:
Input: arr[] = [1, 8, 8, 8, 3, 2]
Output: true
Explanation: The array [1, 8, 8, 8, 3, 2] first increases in the range [0, 1], stays constant in the range [1, 3], and then decreases in the range [3, 4]. Thus, the array is perfect.
Input: arr[] = [1, 1, 2, 2, 1]
Output: false
Explanation: The array does not follow the required pattern of strictly increasing, constant, and then strictly decreasing.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints
1 ≤ arr.size() ≤ 10^6
1 ≤ arr[i] ≤ 10^8
'''

class Solution:
    def isPerfect(self, arr):
        n = len(arr)
        i = 0
        
        while i + 1 < n and arr[i+1] > arr[i]:
            i += 1
            
        while i + 1 < n and arr[i+1] == arr[i]:
            i += 1
            
        while i + 1 < n and arr[i+1] < arr[i]:
            i += 1
            
        return i == n-1
