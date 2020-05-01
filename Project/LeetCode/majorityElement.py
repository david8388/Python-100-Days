from typing import List

# Runtime: 184 ms
# Memory Usage: 15.3 MB


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return max(set(nums), key=nums.count)


problem = Solution()

print(problem.majorityElement([3,3,1,3]))