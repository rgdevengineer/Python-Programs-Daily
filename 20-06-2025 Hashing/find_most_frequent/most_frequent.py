
'''
Find the Most Frequent Element
Return the element that appears the most times in a list.
Example: nums = [1, 2, 3, 2, 2, 4] → 2
'''

def get_input():
    return [1, 2, 3, 2, 2, 4]

def find_most_frequent(nums):
    if not nums:
        return None
    freq = {num: nums.count(num) for num in set(nums)}
    return max(freq, key = freq.get)

def main():
    nums = get_input()
    result = find_most_frequent(nums)
    print(f"The most frequent element is: {result}" if result else "List is empty.")

if __name__ == "__main__":
    main()