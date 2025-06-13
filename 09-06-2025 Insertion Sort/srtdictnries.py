
'''
Given a list of dictionaries, 
sort them by the value of the 'marks' key using Insertion Sort.
Input:
[
  {"name": "A", "marks": 85},
  {"name": "B", "marks": 95},
  {"name": "C", "marks": 80}
]
Output:
[
  {"name": "C", "marks": 80},
  {"name": "A", "marks": 85},
  {"name": "B", "marks": 95}
]

'''

def insertion_sort_dicts_by_key(arr, key):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j][key] > current[key]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr

students = [
    {"name": "A", "marks": 85},
    {"name": "B", "marks": 95},
    {"name": "C", "marks": 80}
]
print(insertion_sort_dicts_by_key(students, "marks"))
