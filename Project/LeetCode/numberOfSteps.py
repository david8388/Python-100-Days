# Runtime: 28 ms
# Memory Usage: 13.9 MB

class Solution:
    def numberOfSteps (self, num: int) -> int:
        count = 0
        while num != 0:
            count += 1
            if num % 2 == 0:
                num = num/2
            else:
                num -= 1
        return count


problem = Solution()

print(problem.numberOfSteps(14))