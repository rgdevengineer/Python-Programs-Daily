
'''
Given a sorted array, print each unique element and its frequency.

Input: [1, 1, 2, 2, 2, 3, 4, 4]
Output: {1: 2, 2: 3, 3: 1, 4: 2}
'''

def frequency_count(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq

print(frequency_count([1, 1, 2, 2, 2, 3, 4, 4]))
