from typing import List

# Runtime: 36 ms
# Memory Usage: 14 MB

#class Solution:
#    def removeElement(self, nums: List[int], val: int) -> int:
#        for i in range(len(nums) -1, -1, -1):
#            if nums[i] == val:
#                del nums[i]
#        return len(nums)

# Runtime: 36 ms
# Memory Usage: 14 MB


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # https://blog.csdn.net/u010558281/article/details/53355211
        for i in nums[:]:
            if i == val:
                nums.remove(i)
        return len(nums)

problem = Solution()

print(problem.removeElement([1, 2, 3, 3, 3, 4], 3))