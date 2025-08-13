
'''
Intersection of Two Sorted Arrays with Distinct Elements

Given two sorted arrays a[] and b[], where each array contains distinct elements , the task is to return the elements in the intersection of the two arrays in sorted order.

Intersection of two arrays can be defined as the set containing distinct common elements that are present in both of the arrays.
Examples:

Input: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3, 6, 7]
Output: 1 2 3
Explanation: Distinct common elements in both the arrays are: 1 2 3
Input: a[] = [2, 3, 4, 5], b[] = [1, 2, 3, 4]
Output: 2 3 4
Explanation: Distinct common elements in both the arrays are: 2 3 4.
Input: a[] = [1], b[] = [2]
Output: []
Explanation: No common elements
Constraints:
1  <=  a.size(), b.size()  <=  105
-109  <=  a[i] , b[i]  <=  109
'''

class Solution:
    def intersection(self, a, b):
        a = set(a)
        b = set(b)
        return sorted(a.intersection(b))