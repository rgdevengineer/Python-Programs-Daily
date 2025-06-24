
'''
Check for Duplicates
Given a list of integers, return True if any value appears more than once.
Example: nums = [1, 2, 3, 1] → True
'''
def has_duplicates(nums):
    element = set()
    for number in nums:
        if number in element:
            return True
        element.add(number)
    return False
