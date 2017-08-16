l = {}

def vertical_traversal(root, level = 0):
    if not root:
        return
    if level not in l:
        l[level] = []
    l[level].append(root.data)
    vertical_traversal(root.left, level-1)
    vertical_traversal(root.right, level+1)

class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

def printTreePath(root, path=[], pathlen=0):
    if not root:
        return
    path.append(root.data)
    if not root.left and not root.right:
        print path
        return
    if root.left:
        printTreePath(root.left, path[:], pathlen+1)
    if root.right:
        printTreePath(root.right, path[:], pathlen+1)

def rootToLeafPath(root, key, path=[]):
    # import pdb; pdb.set_trace()
    if not root:
        return False
    path.append(root.data)

    if root.data == key:
        print path
        return True

    if (root.left and rootToLeafPath(root.left, key, path)) or (root.right and rootToLeafPath(root.right, key, path)):
        # print path
        return True
    path.pop()
    return False



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)

rootToLeafPath(root, 9)
# print l
