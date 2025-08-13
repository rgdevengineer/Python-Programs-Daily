
'''
Dictionary in Python - II

You are now familiar with the dictionary in Python. It's time to dive deeper into the dictionary in Python. How can you use a dictionary to store the frequency of elements in list L. Given below is one method:

for i in L:
     dict[i] = 0

for i in L:
     dict[i] += 1
Now, use this concept to solve a question. Given a list arr[], of positive integers, and an integer sum. The task is to check if any pair exists in the array whose sum is equal to the given sum. If such a pair exists return true, otherwise, return false.

Example:

Input: arr[] = [1, 2, 3, 3, 5], sum = 8 
Output: true
Explanation: Pair with sum 8 is present in the array which is (3, 5).
Input: arr[] = [3, 2, 5], sum = 6 
Output: false
Explanation: No such pair exists in the array.
Constraints:
1 <= arr.size() <= 104
1 <= arr[i], sum <= 104
'''

def pair_sum(dict, arr, sum):
    for i in arr:
        if (sum - i in dict):
            if (sum - i == i):
                if (dict[i] > 1):
                    return True
            else:
                return True

    return False