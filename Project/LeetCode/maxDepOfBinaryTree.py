class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Runtime: 96 ms
# Memory Usage: 15.4 MB


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            leftHeight = 0
            rightHeight = 0
            if root.left != None:
                leftHeight = self.findHeight(root.left)
            if root.right != None:
                rightHeight = self.findHeight(root.right)
            height = leftHeight if leftHeight > rightHeight else rightHeight
            return height + 1

    def findHeight(self, root: TreeNode) -> int:
        leftHeight = 1
        rightHeight = 1
        if root.left != None:
            leftHeight += self.findHeight(root.left)
        if root.right != None:
            rightHeight += self.findHeight(root.right)
        return leftHeight if leftHeight > rightHeight else rightHeight


bt = TreeNode(3)
bt.left = TreeNode(9)
bt.right = TreeNode(20)
bt.right.left = TreeNode(15)
bt.right.right = TreeNode(7)
bt.right.right = TreeNode(7)

problem = Solution()
print(problem.maxDepth(bt))
