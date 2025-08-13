
'''
Dictionary in Python - III

You are familiar with most of the properties of the dictionary in Python. Add some more info about dictionaries through dictionary formatting and deleting key-value pairs.

Formatting:

hash = {}
hash['Geeks'] = 5
hash['geeksforgeeks'] = 13
key = 'Geeks'
s = ("Count of characters is " + 
hash[key] + " in " + key)             
# results in: Count of characters is 
5 in Geeks.
Deleting:

dict = {'a' : 1, 'b': 2, 'c' : 3, 'd' : 4}
del dict['c']          
# delete entry for 'c'
Let's get this into the head by solving a question. Given a list of some students in a list and their corresponding marks in another list. The task is to do some operations as described below:
a. i key value: Iserts key and value in the dictionary, and print 'Inserted'.
b. d key: Delete the entry for a given key and print 'Deleted' if the key to be deleted is present, else print '-1'.
c. key: Print marks of a given key in a statement as "Marks of student name is : marks".

Example:

Input:
N = 5
i geeks 100
i for 200
d geeks
i geeks 300
p geeks
Output:
Inserted
Inserted
Deleted
Inserted
Marks of geeks is 300
Explanation:
For first four queries, insert and del 
operation happens, correspondingly Inserted 
And Deleted is printed. For the last query, 
marks of geeks is printed.
Your Task:
Your task is to complete the function insert_dict(), del_dict() and print_dict() which should perform the operations as required. If nothing is printed for a test case, print "-1".

Constraints:
1 <= N <= 104
1 <= marks <= 104
'''

def insert_dict(query, dict):  # insert into dictionary
    dict[query[1]] = int(query[2])

def del_dict(query, dict): # deleting from dictionary
    if query[1] in dict:
        del dict[query[1]]
        return True
    return False
    
def print_dict(key, dict):  # print marks of required name
    flag = False
    if(key in dict):
        flag = True
        print ("Marks of " + key + " is "+ str(dict[key]))
        
    return True if flag is True else False