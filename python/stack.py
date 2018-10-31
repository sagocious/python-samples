class Stack:
    def __init__(self):
        self.items = []
		
    def push(self, item):
		self.items.append(item)
		
    def pop(self):
		return self.items.pop()
	
    def peek(self):
		return self.items[0]
		
    def isEmpty(self):
		return len(self.items) == 0

## example code
def test():
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print(s.items)
    print(s.pop())
    print(s.items)
    print(s.isEmpty())
#test()
