
'''
Pairs of equals Sum
Given an array arr. Find if there are two pairs (a, b) and (c, d) such that a+b = c+d.

Examples:

Input: arr[] = [3, 4, 7, 1, 2, 9, 8] 
Output: true
Explanation: (3, 7) and (9, 1) are the pairs whosesum are equal.  
Input: arr[] = [65, 30, 7, 90, 1, 9, 8]
Output: false
Explanation: There is no pair.
Constraints:
1 ≤ arr.size() ≤ 103
1 ≤ arr[i] ≤ 104
'''

class Solution:

    def findPairs(self, arr):
        
        n = len(arr)
        Hash = {}

        for i in range(n - 1):
            for j in range(i + 1, n):
                sum = arr[i] + arr[j]
                
                if sum in Hash.keys():
                    return 1
                else:
                    Hash[sum] = (arr[i], arr[j])
        return 0