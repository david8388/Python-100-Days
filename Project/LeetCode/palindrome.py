# Runtime: 88 ms
# Memory Usage: 13.7 MB

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

problem = Solution()

print(problem.isPalindrome(121))