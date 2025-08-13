
'''
Numbered Task List
You’re improving the UX of a task management app by numbering the user’s task list automatically.
Tasks:
Define a function generate_numbered_tasks that takes a list of task names.
Use the enumerate() function to loop through the list with numbering starting from 1.
Format each task as "1. Task Name" and return the final list.
'''

# This function will be tested automatically. 
# Do not change the function name or parameters.
def generate_numbered_tasks(tasks: list[str]) -> list[str]:
    numbered_tasks = []
    for index, task in enumerate(tasks, start = 1):
        numbered_tasks.append(f"{index}. {task}")
    return numbered_tasks