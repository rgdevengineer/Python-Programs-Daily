
'''
Challenge 3: Return Key With Maximum Value
Let's learn to find a key with the maximum value.

Problem Statement
Implement an oldestStudent function that receives the ages dictionary as a parameter, and returns the name of the oldest student.

Input
A dictionary

Output
The key associated with highest age, i.e., the name of the oldest student

Use Python documentation on dictionary to solve the exercise.

Take the following Python dictionary:

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

Key with maximum value => Maria
'''

def oldestStudent(ages):
  max_age = -1
  oldest_name = None
  for name, age in ages.items():
    if age > max_age:
      max_age = age
      oldest_name = name
  return oldest_name
    