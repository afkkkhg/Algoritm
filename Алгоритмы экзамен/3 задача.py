class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def averageOfTree(root):
    sm, current_lvl = root.val, 1
    list_with_roots = [(root)]
    while list_with_roots:
        root = list_with_roots.pop()
        if root.left and root.right:
            sm += root.left.val
            sm += root.right.val
            current_lvl += 2
            list_with_roots.append(root.left)
            list_with_roots.append(root.right)
        elif root.left and not root.right:
            sm += root.left.val
            current_lvl += 1
            list_with_roots.append(root.left)
        elif root.right and not root.left:
            sm += root.right.val
            current_lvl += 1
            list_with_roots.append(root.right)
    return sm/current_lvl
