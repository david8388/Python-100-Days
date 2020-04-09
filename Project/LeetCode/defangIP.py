# Runtime: 28 ms
# Memory Usage: 15 MB


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')


problem = Solution()

print(problem.defangIPaddr('127.0.0.1'))
