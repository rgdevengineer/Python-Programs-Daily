
# Merges two sorted linked lists into one sorted linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_sorted(self, data):
        new_node = Node(data)
        if not self.head or data < self.head.data:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next and current.next.data < data:
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def merge_sorted(list1, list2):
    dummy = Node(0)
    tail = dummy

    a = list1.head
    b = list2.head

    while a and b:
        if a.data < b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next

    tail.next = a or b

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list

# Testing
list1 = LinkedList()
list2 = LinkedList()

for val in [1, 3, 5]:
    list1.insert_sorted(val)

for val in [2, 4, 6]:
    list2.insert_sorted(val)

print("List 1:")
list1.display()
print("List 2:")
list2.display()

merged = merge_sorted(list1, list2)
print("Merged list:")
merged.display()
