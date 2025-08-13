
'''
Difference between highest and lowest occurrence

Given an array, the task is to find the difference between the highest occurrence and lowest occurrence of any number in an array.
Note: If only one type of element is present in the array return 0

Examples:
Input: arr[] = [1, 2, 2]
Output: 1
Explanation:  Lowest occurring element (1) occurs once. Highest occurring element (2) occurs 2 times
Input: arr[] = [7, 8, 4, 5, 4, 1, 1, 7, 7, 2, 5]
Output: 2
Explanation : Lowest occurring element (2) occurs once. Highest occurring element (7) occurs 3 times
Constraints:
1<= arr.size() <=10^6
1<= arr[i] <=10^6
'''

#User function Template for python3

from collections import Counter

class Solution:
    def findDiff(self, arr):
        freq = Counter(arr)
        max_freq = max(freq.values())
        min_freq = min(freq.values())
        
        if max_freq == min_freq:
            return 0
        return max_freq - min_freq
        
    
    
    
    