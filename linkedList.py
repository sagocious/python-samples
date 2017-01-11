class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def insert(self, val):
        newNode = Node(val)
        if self.count == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        self.count += 1

    def insertToEnd(self, val):
        newNode = Node(val)
        if self.count == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.count += 1

    def search(self, val):
        p = self.head
        while p is not None:
            if p.data == val:
                return p
            p = p.next
            
    def delete(self, val):
    	curNode = self.head
    	while curNode != None:
    		if curNode.data == val:
    			if curNode.prev != None:
    				curNode.prev.next = curNode.next
    			else:
    				self.head = curNode.next
    		
    			if curNode.next != None:
    				curNode.next.prev = curNode.prev
    			else:
    				self.tail = curNode.prev
    				
    			self.count -= 1
1    				
    		curNode = curNode.next
    		

    def show(self):
        s = ""
        p = self.head
        while p is not None:
            s += str(p.data) + ' ';
            p = p.next
        print(s + "| count: " + str(self.count))

def test1():
    l = LinkedList()
    l.insert(20)
    l.insert(10)
    l.insertToEnd(30)
    l.insert(5)
    l.insert(9)
    l.show()
    l.delete(20)
    l.show()
    

test1()
