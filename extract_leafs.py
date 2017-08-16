class node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.val = data

class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data


class Tree:
    self.root = None
    self.dlh = None
    self.dlt = None
    self.l = []
    def extract_leaves(self, root):
        if not root.left and not root.right:
            self.l.append(root)
            root = None
            return
        elif root.left:
            self.extract_leaves(root.left)
        elif root.right:
            self.extract_leaves(root.right)
    def appenddl(self, tree_node):
        if not self.dlh and not self.dlt:
            temp = node(tree_node.val):
            self.dlh = temp
            self.dlt = temp
            self.dlh.next = self.dlt
            self.dlt.prev = self.dlh
            return
        else:
            temp = self.dlt
            temp1 = node(tree_node.val)
            temp.next = temp1
            temp1.prev = temp
            self.dlt = temp1
