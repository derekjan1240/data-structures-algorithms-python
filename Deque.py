class Deque(object):

    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        return self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)

d = Deque()
d.addFront(2)
d.addFront(1)
d.addRear(3)
d.addRear(4)
print(d.removeFront(), d.removeRear())
print(d.size(), d.isEmpty())