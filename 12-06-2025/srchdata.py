
# Checks if data is in the list. Returns True or False.

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

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False
    
    def delete(self, key):
        temp = self.head
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            print("Value not found!")
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

print("Search 20:", my_list.search(20))
print("Search 40:", my_list.search(40))



