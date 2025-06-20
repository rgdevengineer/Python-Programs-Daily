
'''
There is a array of 5 elements [1, 3, 2, 1, 3]
find how many times the elements appears in the array?
5
1
4
2
3
12
'''

arr = [1, 3, 2, 1, 3]

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

# for key in freq:
#     print(f"{key} appears = {freq[key]} times")

print('5 appears =', freq.get(5, 0), 'times')
print('1 appears =', freq.get(1, 0), 'times')
print('4 appears =', freq.get(4, 0), 'times')
print('2 appears =', freq.get(2, 0), 'times')
print('3 appears =', freq.get(3, 0), 'times')
print('12 appears =', freq.get(12, 0), 'times')