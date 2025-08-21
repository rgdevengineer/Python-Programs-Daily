
'''
Missing in Array

You are given an array arr[] of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify and return the missing element.

Examples:

Input: arr[] = [1, 2, 3, 5]
Output: 4
Explanation: All the numbers from 1 to 5 are present except 4.
Input: arr[] = [8, 2, 4, 5, 3, 7, 1]
Output: 6
Explanation: All the numbers from 1 to 8 are present except 6.
Input: arr[] = [1]
Output: 2
Explanation: Only 1 is present so the missing element is 2.
Constraints:
1 ≤ arr.size() ≤ 10^6
1 ≤ arr[i] ≤ arr.size() + 1
'''

class Solution:
    def missingNum(self, arr):
        n = len(arr) + 1  # array has n-1 elements, numbers are 1..n
        total = n * (n + 1) // 2
        actual = sum(arr)
        return total - actual
        
        #arr = list(arr)
        #arr.sort()
        # total = 0
        # current = 0
        #l = len(arr)
        # low = arr[0]
        # high = arr[l-1]
        
        # for i in range(arr[0], arr[l-1] + 1):
        #     total += i
            
        # for j in arr:
        #     current += j
            
        # missing_num = total - current
        
        # return missing_num
        
        #arr.sort()
        
        # if not arr:
        #     return None
            
        # arr_set = set(arr)
        
        # for num in range(arr[0], arr[-1] + 1):
        #     if num not in arr_set:
        #         return num
        # return None
        
        
        # if not arr:
        #     return None
            
        # low = min(arr)
        # high = max(arr)
            
        # arr_set = set(arr)
        
        # for num in range(low, high + 1):
        #     if num not in arr_set:
        #         return num
        # return None
        
        
        
        
        
        
        
        
        
        
        
        
        
