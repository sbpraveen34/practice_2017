class node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

    def __unicode__(self):
        return self.data

half_node = []
def half_node_recursive(root):

    if not root:
        return 0
    if (root.left and not root.right) or (not root.left and root.right):
        half_node.append(root.data)
        print id(root)
        return 1 + half_node_recursive(root.left) + half_node_recursive(root.right)
    else:
        return 0 + half_node_recursive(root.left) + half_node_recursive(root.right)

root = node(2)
root.left = node(7)
root.right = node(5)
root.left.right = node(6)
root.left.right.left = node(1)
root.left.right.right = node(11)
root.right.right = node(9)
root.right.right.left = node(4)

print half_node_recursive(root)
for a in half_node:
    print a
