
'''
Challenge 4: Increment Dictionary Values
In this challenge, you are required to increment values in a dictionary.

Problem Statement
Implement an updateAges function that receives ages dictionary and a number n and returns a new dictionary where each student is (n) years older.

Input
A dictionary

Output
Returns a copy of sorted ages where each student is n years older.

Student dictionary (Before increment)

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

n = 1
increment age of all students by 1

Student dictionary (After increment)

| keys    | values |
|---------|--------|
| "Peter" | 11     |
| "Isabel"| 12     |
| "Anna"  | 10     |
| "Thomas"| 11     |
| "Bob"   | 11     |
| "Joseph"| 12     |
| "Maria" | 13     |
| "Gabriel"| 11     |
'''

def updateAges(ages, n):
  for name in ages:
    ages[name] += n
  return ages

