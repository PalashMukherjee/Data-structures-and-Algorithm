class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head= new_node
        self.length +=1
    
    def __str__(self) -> str:
        current_node = self.head
        result = ''
        if self.head == None:
            return 'empty'
        else:
            while current_node is not None:
                result += str(current_node.value)
                current_node = current_node.next
            return result
    def pop(self):
        if self.head is None:
            return 'empty'
        else:
            self.head = self.head.next
    def is_empty(self):
        if self.head is None:
            return 'empty'
        else:
            return 'not empty'
        
s = Stack()
s.append(1)
s.append(2)
s.append(3)
s.append(4)
print(s)
s.pop()
print(s)
s.pop()
print(s)
print(s.is_empty())