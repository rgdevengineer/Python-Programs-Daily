
'''
Shortest un-ordered subarray

Given an array arr of distinct numbers. Find the length of the shortest unordered (neither increasing nor decreasing) subarray in the given array. If there is no subarray then return 0.

Examples:
Input: arr[] = [7, 9, 10, 8, 11]
Output: 3
Explanation: Shortest unsorted subarray is 9, 10, 8 which is of 3 elements.
Input: arr[] = [1, 2, 3, 5]
Output: 0
Explanation: There is no subarray.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= arr.size() <= 10^6
1 <= arr[i] <= 10^5
'''


class Solution:
    def shortestUnorderedSubarray(self, arr):
        n = len(arr)
        
        for i in range(1, n-1):
            if (arr[i-1] < arr[i] > arr[i+1]) or (arr[i-1] > arr[i] < arr[i+1]):
                return 3
        return 0
    
    
    