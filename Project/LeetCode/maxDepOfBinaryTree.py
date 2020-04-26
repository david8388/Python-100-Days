class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Runtime: 76 ms
# Memory Usage: 15.3 MB


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            leftHeight = 0
            rightHeight = 0
            if root.left is not None:
                leftHeight = self.maxDepth(root.left)
            if root.right is not None:
                rightHeight = self.maxDepth(root.right)
            height = leftHeight if leftHeight > rightHeight else rightHeight
            return height + 1


bt = TreeNode(3)
bt.left = TreeNode(9)
bt.right = TreeNode(20)
bt.right.left = TreeNode(15)
bt.right.right = TreeNode(7)
bt.right.right = TreeNode(7)

problem = Solution()
print(problem.maxDepth(bt))
