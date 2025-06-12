
# Implement the Singly Linked List Code

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begining(self, data):  # insert at the begining
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

my_list = SinglyLinkedList()
my_list.insert(10)
my_list.insert(20)
my_list.insert(30)
my_list.insert_begining(5)
my_list.display()
