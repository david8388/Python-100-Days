from typing import List

# Runtime: 36 ms
# Memory Usage: 13.8 MB
# 199. Binary Tree Right Side View

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        rootVal = [root.val]
        right = self.rightSideView(root.right)
        left = self.rightSideView(root.left)
        return rootVal + right + left[len(right):]


problem = Solution()
bt = TreeNode(1)
bt.left = TreeNode(2)
bt.right = TreeNode(3)
bt.left.left = TreeNode(4)
bt.left.right = TreeNode(5)
bt.right.left = TreeNode(6)
bt.right.right = TreeNode(7)
print(problem.rightSideView(bt))
