
# Deletes the first node that contains the given data in Singly Linked List

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
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def insert_begining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        prev = None

        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not Found!")
            return 
        
        if prev is None:
            self.head = temp.next
        else:
            prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

my_list = LinkedList()
my_list.insert(10)
my_list.insert(20)
my_list.insert(30)
my_list.display()

my_list.delete(20)
my_list.display()