
'''
Count the Specials

Given an array arr[] (may contain duplicates) and a positive integer k, your task is to count the number of elements whose occurrence is exactly equal to the size of array arr[] divided by k times.

Examples:

Input: k = 2, arr[] = [1, 4, 1, 2, 4]
Output: 2
Explanation:In the given array, 1 and 4 occurs floor(5/2) = 2 times.So count is 2.
Input: k = 4, arr[] = [1, 1, 7, 1]
Output: 1
Explanation:In the given array, only 7 occurs floor(4/4) = 1 times.So count is 1.
Expected Time Complexity: O(n). 
Expected Auxiliary Space: O(n).

Constraints:
1 <= arr.size() <= 105
1 <= arri <= 106
1 <= k <= arr.size()
'''

from collections import Counter

class Solution:
    def countSpecials(self, k, arr):
        n = len(arr)
        target = n // k  # floor(n / k)

        freq = Counter(arr)  # Count frequency of each element

        count = 0
        for val in freq.values():
            if val == target:
                count += 1

        return count