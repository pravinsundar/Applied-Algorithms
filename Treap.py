import random


class treeNode():

    def __init__(self, data=None, left=None, parent=None, right=None, height=0,priority=0):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.height = height
        self.priority = priority


class Treap():
    def __init__(self, root=None):
        self.root = root

    def get_root(self):
        return self.root

    def insert(self, item):
        if self.root is None:
            self.root = treeNode(item)
            self.root.priority = random.random()

        else:
            new = self.root
            while new is not None:
                if item < new.data:
                    if new.left is None:
                        new.left = treeNode(item)
                        new.left.priority = random.random()
                        new.left.height = 0
                        new.left.parent = new
                        self.updateHeight(new.left.parent)
                        self.siftup(new.left)
                        return
                    else:
                        new = new.left
                else:
                    if new.right is None:
                        new.right = treeNode(item)
                        new.right.priority = random.random()
                        new.right.height = 0
                        new.right.parent = new
                        self.updateHeight(new.right.parent)
                        self.siftup(new.right)
                        return
                    else:
                        new = new.right

    def search(self, node, item):
        if node is None:
            return None
        else:
            if node.data == item:
                return (node)
            elif node.data < item:
                return self.search(node.right, item)
            else:
                return self.search(node.left, item)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)

    def rotate(self, node):
        if (node.parent is None):
            return
        elif (node == node.parent.right):
            self.rotate_left(node)
        else:
            self.rotate_right(node)

    def rotate_right(self, x):
        y = x.parent
        z = x.right
        y_parent = y.parent

        if (y_parent is None):
            x.parent = None
            self.root = x
        elif (y_parent.left == y):
            y_parent.left = x
        else:
            y_parent.right = x

        x.parent = y_parent
        x.right = y
        y.parent = x
        y.left = z

        if (z != None):
            z.parent = y

        self.updateHeight(x)
        self.updateHeight(y)

    def rotate_left(self, x):
        y = x.parent
        z = x.left
        y_parent = y.parent

        if (y_parent is None):
            x.parent = None
            self.root = x

        elif (y_parent.left == y):
            y_parent.left = x

        else:
            y_parent.right = x


        x.parent = y_parent
        x.left = y


        y.parent = x
        y.right = z

        if (z != None):
            z.parent = y

        self.updateHeight(x)
        self.updateHeight(y)

    def updateHeight(self, node):
        if (node is None):
            return

        if (node.left is None):
            lh = 0
        else:
            lh = node.left.height

        if (node.right is None):
            rh = 0
        else:
            rh = node.right.height

        oldHeight = node.height
        newHeight = 1 + max(lh, rh)

        if (oldHeight == newHeight):
            return
        else:
            node.height = newHeight
            self.updateHeight(node.parent)

    def siftup(self,x):
        if(x.parent is None):
                return
        while(x.parent is not None and x.priority >= x.parent.priority):
            if(x.parent is None):
                return
            self.rotate(x)



def build_treap():
    treap = Treap()
    for i in range(100000):
        treap.insert(i)
    print("Root data, Priority, Height", treap.get_root().data,treap.get_root().priority,treap.get_root().height)
    print("Root's left child data, Priority, Height", treap.get_root().left.data,treap.get_root().left.priority,treap.get_root().left.height)
    print("Root's right child data, Priority, Height", treap.get_root().right.data,treap.get_root().right.priority,treap.get_root().right.height)

for i in range(5):
    build_treap()
