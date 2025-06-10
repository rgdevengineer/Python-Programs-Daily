
'''
Sort Students by Marks
Input: A list of tuples like [("Alice", 85), ("Bob", 90), ("Charlie", 75)]
Output: Sorted by marks in ascending order.
'''

lst = [("Alice", 85), ("Bob", 90), ("Charlie", 75)]

name1 = [item[0] for item in lst]
score1 = [item[1] for item in lst]

print("Name: ", name1)
print("Score = ", score1)

def quick_sort(score1):
    if len(score1) <= 1:
        return score1
    else:
        pivot = score1[0]
        lesser = [x for x in score1[1:] if x <= pivot]
        greater = [x for x in score1[1:] if x > pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)

new_score = quick_sort(score1)
# print(new_score)

joined_data = map(lambda n, s: (n, s), name1, new_score)

new_joined_data = list(joined_data)

print(new_joined_data)



