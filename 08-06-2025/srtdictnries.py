
'''
Given a list of dictionaries with 'name' and 'age',
sort by 'age', and if ages are equal, sort alphabetically by 'name'.

Input: [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Anna', 'age': 25}]
Output: [{'name': 'Anna', 'age': 25}, {'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}]
'''

def selection_sort_dicts_multi_key(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if (arr[j]['age'], arr[j]['name']) < (arr[min_idx]['age'], arr[min_idx]['name']):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Anna', 'age': 25}
]
print(selection_sort_dicts_multi_key(data))
