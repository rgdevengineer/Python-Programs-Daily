
'''
Remove duplicates from sorted array 
Given an integer array nums sorted in non-decreasing order, remove all duplicates in-place so that each unique element appears only once. Return the number of unique elements in the array.
If the number of unique elements be k, then,
Change the array nums such that the first k elements of nums contain the unique values in the order that they were present originally.
The remaining elements, as well as the size of the array does not matter in terms of correctness.
An array sorted in non-decreasing order is an array where every element to the right of an element is either equal to or greater in value than that element.
Examples:
Input: nums = [0, 0, 3, 3, 5, 6]
Output: 4
Explanation: Resulting array = [0, 3, 5, 6, _, _]
There are 4 distinct elements in nums and the elements marked as _ can have any value.
Input: nums = [-2, 2, 4, 4, 4, 4, 5, 5]
Output: 4
Explanation: Resulting array = [-2, 2, 4, 5, _, _, _, _]
There are 4 distinct elements in nums and the elements marked as _ can have any value.
'''

class Solution:
    def removeDuplicates(self, number):
        Set = set() # collect unique elements

        for num in number:
            Set.add(num)

        index = 0
        for val in sorted(Set): # sort to maintain order
            number[index] = val
            index += 1

        return index 
    
# Manual Testing

if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    arr1 = [1, 1, 2, 2, 2, 3, 3]
    k1 = sol.removeDuplicates(arr1)
    print("Test Case 1:")
    print("Unique elements:", arr1[:k1])
    print("Count:", k1)
    print()

    # Test Case 2 - already unique
    arr2 = [1, 2, 3, 4]
    k2 = sol.removeDuplicates(arr2)
    print("Test Case 2:")
    print("Unique elements:", arr2[:k2])
    print("Count:", k2)
    print()

    # Test Case 3 - all same elements
    arr3 = [5, 5, 5, 5]
    k3 = sol.removeDuplicates(arr3)
    print("Test Case 3:")
    print("Unique elements:", arr3[:k3])
    print("Count:", k3)
    print()

    # Test Case 4 - empty array
    arr4 = []
    k4 = sol.removeDuplicates(arr4)
    print("Test Case 4:")
    print("Unique elements:", arr4[:k4])
    print("Count:", k4)
    print()

    # Test Case 5 - single element
    arr5 = [42]
    k5 = sol.removeDuplicates(arr5)
    print("Test Case 5:")
    print("Unique elements:", arr5[:k5])
    print("Count:", k5)