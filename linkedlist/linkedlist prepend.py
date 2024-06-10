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

    def __str__(self):
        temp_node = self.head 
        result =''
        while temp_node is not None:
            result += str(temp_node.value)+'=>'
            temp_node=temp_node.next
        return result

    def prepend(self,value):
        new_node= Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1

    def insert(self, index, value):
        new_node = Node(value)
        temp_node = self.head
        if index <0 or index >self.length:
            return False
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif index==0:
            new_node.next = self.head.next
            self.head = new_node
        else:
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length +=1


ll = linkedlist()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.prepend(0)
ll.prepend(-1)
ll.insert(2,0.5)
ll.insert(3,0.7)
print(ll)