from typing import List

# Runtime: 44 ms
# Memory Usage: 11.4 MB

# Using built-in function
#class Solution:
#    def findMin(self, nums: List[int]) -> int:
#        return min(nums)

# Runtime: 44 ms
# Memory Usage: 14.3 MB

class Solution:
    def findMin(self, nums: List[int]) -> int:
        first, last = 0, len(nums) - 1
        while first < last:
            mid = (first + last) // 2
            if nums[mid] > nums[last]:
                first = mid + 1
            else:
                last = mid
        return nums[first]


problem = Solution()

print(problem.findMin([3, 4, 5, 1, 2]))