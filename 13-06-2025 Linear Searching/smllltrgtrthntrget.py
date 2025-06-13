
'''
Find smallest letter greater than target

Description:
You are given a sorted array of characters letters, sorted in non-decreasing order, and a character target. 
There are at least two different characters in letters. Your task is to return the smallest character in letters that is lexicographically greater than target. 
If such a character does not exist, return the first character in letters.
Input:
letters: A sorted array of characters in non-decreasing order.
target: A character to compare against.
Output:
Return the smallest character that is greater than target. If no such character exists, return the first character in letters.
'''

def next_greatest_letter(letters, target):
    
    left, right = 0, len(letters)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if letters[mid] > target:
            right = mid
        else:
            left = mid + 1
    
    return letters[left % len(letters)]

# letters = ['c', 'f', 'j']
# target = 'k'
 
# letters = ['c', 'f', 'j']
# target = 'c'

# letters = ['c', 'f', 'j']
# target = 'a'

print(next_greatest_letter(['c', 'f', 'j'], 'k'))  
print(next_greatest_letter(['c', 'f', 'j'], 'c'))  
print(next_greatest_letter(['c', 'f', 'j'], 'a'))  
print(next_greatest_letter(['a', 'b'], 'z'))       
print(next_greatest_letter(['e', 'e', 'e', 'k', 'q', 'q'], 'e'))  
