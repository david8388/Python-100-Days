from typing import List

# Runtime: 8900 ms
# Memory Usage: 16.2 MB


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            newNums = nums[:i] + nums[i+1:]
            if nums[i] not in newNums:
                return nums[i]


problem = Solution()

print(problem.singleNumber([3, 0, 3]))
