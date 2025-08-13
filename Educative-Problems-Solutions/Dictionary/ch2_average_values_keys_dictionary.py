
'''
Challenge 2: Average of Values of Keys in a Dictionary
In this challenge, you are required to calculate the average of values in a dictionary.

Problem Statement
Implement a calculateAvg function that receives the ages dictionary as a ​parameter, and returns the average age of the students. Traverse all items in the dictionary using the “items” method above.

Input
A dictionary

Output
The average age of all students in the dictionary

Student dictionary

| keys    | values |
|---------|--------|
| "Peter" | 10     |
| "Isabel"| 11     |
| "Anna"  | 9      |
| "Thomas"| 10     |
| "Bob"   | 10     |
| "Joseph"| 11     |
| "Maria" | 12     |
| "Gabriel"| 10     |

Average age = sum of all ages / total keys = 10.375
'''

def calculateAvg(ages):
  total = 0
  count = 0
  for name, age in ages.items():
    total += age
    count += 1
  if count == 0:
    return 0
  return total / count