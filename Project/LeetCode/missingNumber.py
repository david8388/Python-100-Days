from typing import List


# Runtime: 140 ms
# Memory Usage: 14.9 MB

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for idx, num in enumerate(nums):
            if idx != num:
                return idx
        if len(nums) not in nums:
            return len(nums)


problem = Solution()

print(problem.missingNumber([3, 0, 1]))
