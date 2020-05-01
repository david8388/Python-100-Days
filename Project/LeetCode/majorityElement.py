from typing import List
# 169. Majority Element
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# Runtime: 184 ms
# Memory Usage: 15.3 MB

#class Solution:
#    def majorityElement(self, nums: List[int]) -> int:
#        return max(set(nums), key=nums.count)

# Runtime: 180 ms
# Memory Usage: 15.3 MB

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate

problem = Solution()

print(problem.majorityElement([1,2,3,2,2]))