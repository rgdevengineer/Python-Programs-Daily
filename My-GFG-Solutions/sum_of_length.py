
'''
Sum of length
Given an array arr. Calculate the sum of lengths of contiguous subarrays having all distinct elements.
Note: Return the answer with modulo 109+7.

Examples:

Input: arr[] = [1, 2, 3]
Output: 10
Explanation: [1, 2, 3] is a subarray of length 3 with distinct elements. [1, 2], [2, 3] are 2 subarray of length 2 with distinct elements. Total length of lengths two = 2 + 2 = 4  3 subarrays of length 1 with distinct element. Sum of lengths = 3 + 4 + 3 = 10
Input: arr[] = [1]
Output: 1
Explanation: The only subarray with distinct elements of length 1.  
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 106
'''

class Solution:
    def sumoflength(self, arr):
        MOD = 10**9 + 7
        n = len(arr)
        seen = set()
        left = 0
        total_length = 0

        for right in range(n):
            while arr[right] in seen:
                seen.remove(arr[left])
                left += 1

            seen.add(arr[right])

            length = right - left + 1
            total_length = (total_length + (length * (length + 1)) // 2) % MOD

        return total_length