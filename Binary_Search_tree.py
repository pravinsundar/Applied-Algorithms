file = open('6_test_BST.txt', 'r').read().strip()
l = file.split("\n")
A = [int(i) for i in l[1:]]
print(A)

n = A[0]
B = A[1:]

class treeNode():
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BST():
    def __init__(self, root=None):
        self.root = root

    def get_root(self):
        return self.root

    def insert(self, item):
        if self.root is None:
            self.root = treeNode(item)
        else:
            new = self.root
            while new is not None:
                if item < new.data:
                    if new.left is None:
                        new.left = treeNode(item)
                        return
                    else:
                        new = new.left
                else:
                    if new.right is None:
                        new.right = treeNode(item)
                        return
                    else:
                        new = new.right

    def search(self, node, item):
        if node is None:
            return False
        else:
            if node.data == item:
                return True
            elif node.data < item:
                return self.search(node.right, item)
            else:
                return self.search(node.left, item)


    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print (node.data)
            self.inorder(node.right)

c = BST()

for i in range(n):
    c.insert(B[i])

for i in range(n):
    c.insert(B[i])

count = 0

for i in range(101):
    x = c.search(c.get_root(),i)
    if x:
        count = count +1

print(count)
