class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
    def pop_first(self):
        if self.head == None:
            return 'no new node'
        else:
            self.head = self.head.next
    def __str__(self):
        current_node = self.head
        result = ''
        while current_node is not None:
            result += str(current_node.value)
            current_node=current_node.next
            if current_node == self.head:
                break
        return result

q = queue()
q.append(1)
q.append(2)
q.append(3)
q.append(4)
print(q)
q.pop_first()
q.pop_first()
print(q)