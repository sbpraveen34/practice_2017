def diameter_of_binary_tree(root):
    if not root:
        return 0

    ll = diameter_of_binary_tree(root.left)
    lr = diameter_of_binary_tree(root.right)
    return max([1+ll, 1+lr, ll+lr+1])
