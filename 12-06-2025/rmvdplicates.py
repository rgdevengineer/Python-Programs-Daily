
# Remove Duplicates from an Unsorted Linked Lis

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_duplicates(self):
        current = self.head
        seen = set()
        prev = None
        while current:
            if current.data in seen:
                prev.next = current.next
            else:
                seen.add(current.data)
                prev = current
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Testing
my_list = LinkedList()
for val in [10, 20, 10, 30, 20, 40]:
    my_list.insert(val)

print("Before removing duplicates:")
my_list.display()

my_list.remove_duplicates()

print("After removing duplicates:")
my_list.display()
