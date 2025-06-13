
'''
You're given a list of dictionaries where each dictionary has a 'name' and 'age'. 
Sort the list by 'age' using Bubble Sort.

Input: [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
Output: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}]
'''

def bubble_sort_dicts(arr, key):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][key] > arr[j + 1][key]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
print(bubble_sort_dicts(people, 'age'))
