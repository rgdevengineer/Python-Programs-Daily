
# Implementation of Stack using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return "Stack Underflow"
        popped = self.top.data
        self.top = self.top.next
        return popped
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    
    def display(self):
        current = self.top
        print("Stack (top -> bottom): ", end='')
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

s = StackLinkedList()
s.push(10)
s.push(20)
s.push(30)
s.display()

print("Top:", s.peek())
print("Popped:", s.pop())
        

