class node:
    def __init__(self, n):
        self.val = n
        self.left = None
        self.right = None

class BST:
    def insertUtil(self, root, n):
        if not root:
            root = node(n)
        else:
            if root.val < n:
                self.insertUtil(root.right, n)
            elif root.val > n:
                self.insertUtil(root.left, n):
            else:
                print "duplicate Node"
                return

    def search(self, root, n):
        if not root:
            print "Node not found"
            return
        else:
            if root.val < n:
                self.search(root.right, n)
            elif root.val > n:
                self.search(root.left, n)
            else:
                return root

    def getInorderSuccessor(self, root):
        temp = root
        while(temp and temp.left):
            temp = temp.left
        return

    def delete(self, root, n):
        if not root:
            return
        else:
            del_root = self.search(root, n)
            if del_root.left and del_root.right:
            elif del_root.left:
                del_root = del_root.left
            elif del_root.right:
                del_root = del_root.right
            else:
                print del_root.val
                del_root = None
