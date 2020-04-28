from typing import List


class Solution:

    # Runtime: 4028 ms
    # Memory Usage: 14.2 MB
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #    for idx, num in enumerate(numbers):
    #        aim = target - num
    #        nextIdx = idx + 1
    #        if aim in numbers[nextIdx:]:
    #            aimIndex = numbers[nextIdx:].index(aim) + nextIdx
    #            return [idx + 1, aimIndex + 1] # Not zero-based
    #    return []

    # Runtime: 64 ms
    # Memory Usage: 14.4 MB

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum > target:
                right -= 1
            else:
                left += 1


problem = Solution()

print(problem.twoSum([0, 0, 2, 3, 4], 2))
