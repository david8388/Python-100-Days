from typing import List


# Runtime: 4028 ms
# Memory Usage: 14.2 MB

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx, num in enumerate(numbers):
            aim = target - num
            nextIdx = idx + 1
            if aim in numbers[nextIdx:]:
                aimIndex = numbers[nextIdx:].index(aim) + nextIdx
                return [idx + 1, aimIndex + 1] # Not zero-based
        return []


problem = Solution()

print(problem.twoSum([2, 98, 0, 0, 3, 4], 0))