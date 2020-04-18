# Runtime: 24 ms
# Memory Usage: 13.6 MB

class Solution:
    def reverse(self, x: int) -> str:
        limit = pow(2, 31)
        sign = 1 if x >= 0 else -1
        result = int(str(abs(x))[::-1])
        if result > (limit - 1) or result < (limit * -1):
            return 0
        return result * sign

problem = Solution()

print(problem.reverse(1534236469))