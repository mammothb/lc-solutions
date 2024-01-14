class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        result = []
        n = len(pattern)
        for i in range(n + 1):
            stack.append(i + 1)
            if i == n or pattern[i] == "I":
                while stack:
                    result.append(stack.pop())
        return "".join(map(str, result))
