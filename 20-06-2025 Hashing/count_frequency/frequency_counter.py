
'''
Count Frequency of Elements
Given a list of integers, return a dictionary where each key is a number and the value is its count.
Example: nums = [1, 2, 2, 3, 3, 3] → {1:1, 2:2, 3:3}
'''

def count_frequency(numbers):
    freq_map = {}
    for num in numbers:
        if num in freq_map:
            freq_map[num] += 1  
        else:
            freq_map[num] = 1
    return freq_map

