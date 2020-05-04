from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        rightVal = []
        cur = []
        if root is not None:
            if root.val:
                rightVal.append(root.val)
            if root.right:
                cur = self.rightSideView(root.right)
                rightVal.extend(cur)
            elif root.left:
                left = self.rightSideView(root.left)
                rightVal.extend(left)
        return rightVal


#problem = Solution()
#tn = TreeNode(1)
#tn.left(TreeNode(2))
#tn.right(TreeNode(3))
#tn.left(TreeNode(2)).left(TreeNode(4))
#print(tn)
# print(problem.rightSideView(tn))