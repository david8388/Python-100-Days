from typing import List

# Runtime: 60 ms
# Memory Usage: 14.2 MB

class Solution:
    def findMin(self, nums: List[int]) -> int:
        first, last = 0, len(nums) - 1
        while first < last:
            mid = (first + last) // 2
            if nums[mid] > nums[last]:
                first = mid + 1
            else:
                last = mid if nums[mid] != nums[last] else last - 1
        return nums[first]


problem = Solution()

print(problem.findMin([3,3,1,3]))
print(problem.findMin([1,3,3]))