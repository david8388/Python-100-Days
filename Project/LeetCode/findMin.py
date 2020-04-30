from typing import List

# Runtime: 44 ms
# Memory Usage: 11.4 MB


class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)


problem = Solution()

print(problem.findMin([3, 4, 5, 1, 2]))