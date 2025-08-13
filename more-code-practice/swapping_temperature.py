
'''
Swapping Temperature
You are building a temperature converter app. Sometimes, due to incorrect input order, the min_temp and max_temp values are swapped.

Current values are

min_temp = 40
max_temp = 25

Use Python tuples to swap them back to the correct order.
'''

min_temp = 40
max_temp = 25

min_temp, max_temp = max_temp, min_temp

print(min_temp)
print(max_temp)