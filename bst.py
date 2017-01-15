class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

    def insert(self, val):
        if val < self.value:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        elif val > self.value:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert(val)

    def lookup(self, val, parent=None):
        if val < self.value:
            if self.left is None:
                return None, None
            return self.left.lookup(val, self)
        elif val > self.value:
            if self.right is None:
                return None, None
            return self.right.lookup(val, self)
        else:
            return self, parent


    def children_count(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count

    def delete(self, val):
        node, parent = self.lookup(val)
        if self.children_count() == 0:
            if parent:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                del node
            else:
                self.value = None

        elif self.children_count() == 1:
            if node.left:
                n = node.left
            else:
                n = node.right
            if parent:
                if parent.left is node:
                    parent.left = n
                else:
                    parent.right = n
                del node
            else:
                self.left = n.left
                self.right = n.right
                self.value = n.value

        else:
            parent = node
            successor = node.right
            while successor.left is not None:
                parent = successor
                successor = successor.left

            node.value = successor.value
            if parent.left == successor:
                parent.left = successor.right
            else:
                parent.right = successor.right

    def pre_order(self):
        print self.value,
        if self.left is not None:
            self.left.pre_order()
        if self.right is not None:
            self.right.pre_order()

    def in_order(self):
        if self.left is not None:
            self.left.in_order()
        print self.value,
        if self.right is not None:
            self.right.in_order()

    def post_order(self):
        if self.left is not None:
            self.left.post_order()
        if self.right is not None:
            self.right.post_order()
        print self.value,

##test
t = Node(10)
t.insert(2)
t.insert(15)
t.insert(5)
t.delete(5)
t.post_order()
