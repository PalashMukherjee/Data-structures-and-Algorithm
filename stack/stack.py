class stack:
    def __init__(self):
        self.list = []
    def __str__(self):
        values = [str(x) for x in self.list]
        return ' '.join(values)
    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False
    def push(self,value):
        self.list.append(value)
    def print_list(self):
        return self.list
    def peek(self):
        if self.is_empty():
            return 'stack is empty'
        else:
            return self.list[len(self.list)-1]
    def pop(self):
        if self.is_empty():
            return 'stack is empty'
        else:
            self.list.pop()

s = stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s)
s.pop()
s.pop()
print(s)
