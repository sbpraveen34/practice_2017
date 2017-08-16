class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self, root_key):
        self.root = Node(root_key)
        self.tree_len = 1
        self.prev = None
        self.suc = None

    def insert(self, root, node):
        if root == None:
            root = node;
            return
        else:
            if node.key < root.key:
                if root.left is None:
                    root.left = node
                else:
                    self.insert(root.left, node)
            elif node.key > root.key:
                if root.right == None:
                    root.right = node
                else:
                    self.insert(root.right, node)
    def print_tree(self, root):
        if root:
            self.print_tree(root.left)
            print root.key
            self.print_tree(root.right) 

    def inorderSuccessor(self, root, key):
        if(root.key == key):
            if root.left:
                temp = root.left
                while temp.right:
                    temp = temp.right
                self.prev = temp
            if root.right:
                temp2 = root.right
                while temp2.left:
                    temp2 = temp2.left
                self.suc = temp2
            return
        elif root.key > key:
            self.suc = root
            self.inorderSuccessor(root.left, key)
        else:
            self.prev = root
            self.inorderSuccessor(root.right, key)


a = BST(2)
a.insert(a.root, Node(1))
a.insert(a.root, Node(3))
a.insert(a.root, Node(4))
a.insert(a.root, Node(5))
a.insert(a.root, Node(6))
a.insert(a.root, Node(7))
a.print_tree(a.root)
import pdb; pdb.set_trace()
a.inorderSuccessor(a.root, 4)
print a.prev.key
print a.suc.key
