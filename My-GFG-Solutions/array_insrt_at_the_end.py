
'''
Array insert at end
Difficulty: BasicAccuracy: 87.65%Submissions: 67K+Points: 1
Given an array arr that is not completely filled and a value a, you have to insert the value at the end of the array.

Examples :

Input: arr[] = [1, 2, 3, 4, 5], val = 90
Output: [1, 2, 3, 4, 5, 90]
Explanation: After inserting 90 at the end, we have array elements as 1 2 3 4 5 90.
Input: arr[] = [1, 2, 3], val = 50
Output: [1, 2, 3, 50]
Explanation: After inserting 50 at the end, we have array elements as 1 2 3 50.
Constraints:
1 ≤ arr.size() ≤ 10^5
0 ≤ element, arr[i] ≤ 10^6
'''

class Solution:
    def insertAtEnd(self, arr, val):
        arr.append(val)
        return arr