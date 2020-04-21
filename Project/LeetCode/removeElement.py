from typing import List

# Runtime: 36 ms
# Memory Usage: 14 MB

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums) -1, -1, -1):
            if nums[i] == val:
                del nums[i]
        return len(nums)


problem = Solution()

print(problem.removeElement([3, 2, 2, 3], 3))