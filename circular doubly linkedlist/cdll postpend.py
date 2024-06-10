class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class Circular_Doubly_Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length  = 0

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            new_node.prev = self.tail
            self.tail.next = new_node
        self.length +=1

    def __str__(self):
        current_node= self.head
        result = ''
        while current_node is not None:
            result += str(current_node.value)
            current_node= current_node.next
            if current_node == self.head:
                break
        return result
    
    def postpend(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            new_node.next = self.head
        self.length +=1
    
    def traverse(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break
    
    def reverse_traverse(self):
        current_node = self.tail
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.prev
            if current_node == self.tail:
                break


cdll = Circular_Doubly_Linkedlist()
cdll.append(1)
cdll.append(2)
cdll.append(3)
cdll.append(4)
print(cdll)
cdll.postpend(0)
cdll.postpend(-1)
cdll.postpend(-2)
print(cdll)
cdll.traverse()


