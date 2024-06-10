class Node:
    def __init__(self, value):
        self.value = value
        self.next=None

class linkedlist:
    def __init__(self):
        self.head = None
        self.next = None
        self.length =1

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1

ll = linkedlist()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
print(ll)