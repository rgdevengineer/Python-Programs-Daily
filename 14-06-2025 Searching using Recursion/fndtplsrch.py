
'''
Tuple Search with Key-Value Match
Description:
You are given a list of tuples where each tuple contains (employee_id, department).
Find the index of the tuple where the department is "HR".
data = [(101, "IT"), (102, "HR"), (103, "Sales")] 
'''

def find_HR(data):
    for index, (emp_id, dept) in enumerate(data):
        if dept == "HR":
            return index
        
    return -1

data = [(101, "IT"), (102, "HR"), (103, "Sales")]

data_found = find_HR(data)

print("The HR will be at", data_found, "postion")