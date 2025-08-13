
'''
Challenge 6: Average Values Within Multiple Dictionaries
In this challenge, you are required to average values of a single key within multiple dictionaries.

Problem Statement
Implement a calculateAverageAge function that receives the students dictionary and returns the average age.

Input
A nested dictionary

Output
The average age of students
Student dictionary

| keys    | subkeys | subvalues |
|---------|---------|-----------|
| "Peter" | age     | 10        |
|         | address | "Lisbon"  |
| "Susan" | age     | 11        |
|         | address | "Sweden"  |
| "Charles"| age     | 9         |
|         | address | "Turkey"  |
| "Thomas"| age     | 10        |
|         | address | "Lisbon"  |
| "Bob"   | age     | 11        |
|         | address | "Sweden"  |
| "Joseph"| age     | 9         |
|         | address | "Turkey"  |

Average age of Students = (10 + 11 + 9 + 10 + 11 + 9) / 6 = 10
'''

def calculateAverageAge(students):
  total_age = 0
  count = 0
  
  for student in students.values():
    if 'age' in student:
      total_age += student['age']
      count += 1
      
  if count == 0:
    return 0
  return total_age / count