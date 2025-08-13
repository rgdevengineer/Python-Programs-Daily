
'''
Challenge 7: Keys Matching in Multiple Dictionaries
In this challenge, you are required to find keys matching a given value from multiple dictionaries.

Problem Statement
Implement a find_students function that receives the students dictionary and an address, and returns a list with names of all students whose address matches the address in the argument. For instance, invoking find_students('Lisbon') should return Anna and Peter. Also, note that the names should be printed in alphabetical order.

Input
A nested dictionary students and address

Output
The keys matching the address in the sorted order, i.e., the name of the students living in a particular area

Student dictionary

| keys    | subkeys | subvalues |
|---------|---------|-----------|
| "Peter" | age     | 21        |
|         | address | "Lisbon"  |
| "Anna"  | age     | 22        |
|         | address | "Lisbon"  |
| "Charles"| age     | 32        |
|         | address | "Turkey"  |

address = "Lisbon"
Output = ['Anna', 'Peter']
'''
def find_students(address, students):
  matching_students = []
  for name, info in students.items():
    if 'address' in info and info['address'] == address:
      matching_students.append(name)
  return sorted(matching_students)

