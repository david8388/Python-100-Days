from typing import List

# Runtime: 52 ms
# Memory Usage: 14.6 MB

#class Solution:
#    def searchInsert(self, nums: List[int], target: int) -> int:
#        nums.append(target)
#        nums.sort()
#        return nums.index(target)

# Runtime: 56 ms
# Memory Usage: 14.4 MB


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, el in enumerate(nums):
            if target <= el:
                return i
        return len(nums)


problem = Solution()

print(problem.searchInsert([0, 1, 3], 5))
