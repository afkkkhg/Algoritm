# class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
    stack = [root]
    lst = []
    while stack:
        ptr = stack.pop()
        if ptr.left:
            stack.append(ptr.left)
            lst.append((ptr.left).val)
        if ptr.right:
            stack.append(ptr.right)
            lst.append((ptr.right).val)
    min_v = 10 ** 6
    lst.append(root.val)
    lst.sort()
    for i in range(len(lst)):
        if min_v > abs(lst[i - 1] - lst[i]):
            min_v = abs(lst[i - 1] - lst[i])
    return min_v

