import collections
from typing import List

# Runtime: 36 ms
# Memory Usage: 13.8 MB
# 199. Binary Tree Right Side View

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#class Solution:
#    def rightSideView(self, root: TreeNode) -> List[int]:
#        if root is None:
#            return []
#        rootVal = [root.val]
#        right = self.rightSideView(root.right)
#        left = self.rightSideView(root.left)
#        return rootVal + right + left[len(right):]

# Runtime: 36 ms
# Memory Usage: 13.9 MB

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        result = []
        queue = collections.deque([root])
        while queue:
            size = len(queue)
            last_node = None
            for _ in range(size):
                node = queue.popleft()
                print(node.val)
                last_node = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if last_node:
                result.append(last_node.val)
        return result


problem = Solution()
bt = TreeNode(1)
bt.left = TreeNode(2)
bt.right = TreeNode(3)
bt.left.left = TreeNode(4)
bt.left.right = TreeNode(5)
bt.right.left = TreeNode(6)
bt.right.right = TreeNode(7)
print(problem.rightSideView(bt))
