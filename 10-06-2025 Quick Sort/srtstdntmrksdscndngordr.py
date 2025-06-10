
'''
Sort Students by Marks
Input: A list of tuples like [("Alice", 85), ("Bob", 90), ("Charlie", 75)]
Output: Sorted by marks in descending order.
'''

lst = [("Alice", 85), ("Bob", 90), ("Charlie", 75)]

name2 = [item[0] for item in lst]
score2 = [item[1] for item in lst]

print("Name: ", name2)
print("Score = ", score2)

def quick_sort(score2):
    if len(score2) <= 1:
        return score2
    else:
        pivot = score2[0]
        greater = [x for x in score2[1:] if x >= pivot]
        lesser = [x for x in score2[1:] if x < pivot]
        return quick_sort(greater) + [pivot] + quick_sort(lesser)
    
new_score = quick_sort(score2)
print(new_score)

combined_data = map(lambda n, s: (n, s), name2, new_score)

new_combined_data = list(combined_data)

print(new_combined_data)

'''
combined_data = []

for i in range(len(name2)):
    current_tuple = (name2[i], score2[i])   # this for loop method is not working correctly
    combined_data.append(current_tuple)

print(combined_data)
'''