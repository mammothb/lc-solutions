class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        stack = []
        for i in range(n):
            if s[i] == "(":
                stack.append(i)
            else:
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(i)
        if not stack:
            return n
        stop = n
        result = 0
        while stack:
            result = max(result, stop - 1 - stack[-1])
            stop = stack.pop()

        return max(result, stop)
