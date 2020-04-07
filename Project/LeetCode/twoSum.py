from typing import List


class Solution:
    # Runtime: 5812 ms
    # Memory Usage: 15 MB
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     length = len(nums)
    #     output = []
    #     for x in range(length):
    #         for y in range(x + 1, length):
    #             print('x {}, y {}'.format(x, y))
    #             if nums[x] + nums[y] == target:
    #                 output = [x, y]
    #                 break;
    #         if len(output) != 0:
    #             print('In')
    #             return output

    # Runtime: 104 ms
    # Memory Usage: 15 MB
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for idx, value in enumerate(nums):
            print(idx, value)
            if target - value in index:
                return [index[target - value], idx]
            index[value] = idx


problem = Solution()

print(problem.twoSum([2, 7, 11, 15], 9))