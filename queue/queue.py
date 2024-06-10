class queue:
    def __init__(self):
        self.list = []
    def __str__(self) -> str:
        self.list = [str(x) for x in self.list]
        return ' '.join(self.list)
    def append(self,value):
        self.list.append(value)
        return self
    def delete(self):
        self.list.pop(0)
        return self
q = queue()
q.append(1)
q.append(2)
q.append(3)
q.append(4)
print(q.append(5))

