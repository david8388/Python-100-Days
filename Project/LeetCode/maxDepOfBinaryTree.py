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
            leftHeight = self.maxDepth(root.left)
            rightHeight = self.maxDepth(root.right)
            return max(leftHeight, rightHeight) + 1


bt = TreeNode(3)
bt.left = TreeNode(9)
bt.right = TreeNode(20)
bt.right.left = TreeNode(15)
bt.right.right = TreeNode(7)
bt.right.right = TreeNode(7)

problem = Solution()
print(problem.maxDepth(bt))
