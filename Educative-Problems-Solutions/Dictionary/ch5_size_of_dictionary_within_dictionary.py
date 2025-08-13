
'''
Challenge 5: Size of a Dictionary Within a Dictionary
In this challenge, your task is to calculate the size of the dictionary within a dictionary.

Problem Statement​
Given a totalStudents function, your task is to calculate how many students are in the students dictionary.

Input
A nested dictionary

Output
The size of the nested dictionary

Student dictionary

| keys    | subkeys | subvalues |
|---------|---------|-----------|
| "Peter" | age     | 21        |
|         | address | "Lisbon"  |
| "Susan" | age     | 22        |
|         | address | "Sweden"  |
| "Charles"| age     | 32        |
|         | address | "Turkey"  |

Size of Student = 3
'''

def totalStudents(students):
  return len(students)