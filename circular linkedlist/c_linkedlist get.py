class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class CSlinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length+=1
    def __str__(self):
        temp_node = self.head 
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += '=>'
        return result
        
    def prepend(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.tail.next = new_node
        self.head = new_node

    def insert(self, index, value):
        new_node = Node(value)
        current_node = self.head
        if index == 0:
            new_node.next = self.head
            self.tail.next = new_node
        else:
            for _ in range(index-1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
        self.length+=1
    
    def traversal(self):
        current_node = self.head 
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next
            if current_node == self.head :
                break

    def search(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                print('found')
            current_node = current_node.next
            if current_node == self.head:
                break

    def get(self,index):
        current_node = self.head
        for _ in range(index-1):
            current_node = current_node.next
        return current_node

    def set(self,index,value):
        self.get(index).value = value
        return self
    
    def delete_first(self):
        self.head = self.head.next
        self.tail.next = self.head
        return self

csll = CSlinkedlist()
csll.append(1)
csll.append(2)
csll.append(3)
csll.append(4)
print(csll.length)
print(csll)
csll.prepend(0)
csll.prepend(-1)
print(csll)
csll.insert(2,0.5)
print(csll)
csll.insert(4,1.5)
# print(csll)
# csll.traversal()
# csll.search(4)
# csll.search(1.5)
print(csll.get(3))
print(csll.set(2,-0.5))
print(csll)
print(csll.delete_first())
print(csll.delete_first())
