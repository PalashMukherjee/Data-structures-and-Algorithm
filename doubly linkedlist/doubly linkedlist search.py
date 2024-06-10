class Node:
    def __init__(self,value):
        self.next = None
        self.prev = None
        self.value = value
    def __str__(self):
        return str(self.value)
    
class Doubly_Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length +=1

    def __str__(self):
        current_node = self.head 
        result = ''
        while current_node is not None:
            result += str(current_node.value)
            current_node = current_node.next
            result += '=>'
        return result 
    def prepend(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

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

    def search(self,value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    def get(self,index):
        current_node = self.head
        for _ in range(index-1):
            current_node = current_node.next
        return current_node.value


dll = Doubly_Linkedlist()
dll.append(1)
dll.append(2)
dll.append(3)
print(dll)
dll.prepend(0)
dll.prepend(-1)
print(dll)
dll.prepend(-2)
print(dll)
# dll.traverse()
dll.reverse_traverse()
print(dll.search(6))
print(dll.get(4))