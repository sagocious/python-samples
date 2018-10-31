from queue import *

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

    def insert(self, val):
        if val < self.data:
            if self.left == None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        else:
            if self.right == None:
                self.right = Node(val)
            else:
                self.right.insert(val)

def preorderTrav(node):
    if node is not None:
        print(node.data)
        preorderTrav(node.left)
        preorderTrav(node.right)

def inorderTrav(node):
    if node is not None:
        inorderTrav(node.left)
        print(node.data)
        inorderTrav(node.right)

def postorderTrav(node):
    if node is not None:
        postorderTrav(node.left)
        postorderTrav(node.right)
        print(node.data)
    
def breathFirstTrav(tree):
    q = Queue()
    q.enqueue(tree)

    while not q.isEmpty():
        node = q.dequeue()
        print(node.data)
        if node.left is not None:
            q.enqueue(node.left)
        if node.right is not None:
            q.enqueue(node.right)

##test
t = Node(10)
t.insert(2)
t.insert(15)
t.insert(5)
preorderTrav(t)
print("\n")
print("\n")
breathFirstTrav(t)
