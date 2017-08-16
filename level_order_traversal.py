from collections import defaultdict

c = defaultdict(list)

def level_order_traversal(root, current_level=0):
    if not root:
        return
    c[current_level].append(root)
    level_order_traversal(root.left, current_level+1)
    level_order_traversal(root.right, current_level+1)
