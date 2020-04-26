from typing import List
from collections import Counter


# Runtime: 932 ms
# Memory Usage: 15.3 MB

# class Solution:
#    def singleNumber(self, nums: List[int]) -> int:
#        no = []
#        for index, num in enumerate(nums):
#            if num not in nums[index+1:] and num not in no:
#                return num
#            else:
#                no.append(num)

# Runtime: 56 ms
# Memory Usage: 15.3 MB

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = Counter(nums)
        for index, num in enumerate(s):
            if s[num] == 1:
                return num


problem = Solution()

print(problem.singleNumber([2, 2, 3, 2]))
