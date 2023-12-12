class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        result = 0
        sign = 1
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c in "+-":
                result += sign * num
                sign = 1 if c == "+" else -1
                num = 0
            elif c == "(":
                # temporarily store result and reset
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif c == ")":
                # Finish processing the current equation
                result += sign * num
                sign = stack.pop()
                prev = stack.pop()
                # process result in parentheses and prev result
                result = prev + sign * result
                num = 0

        result += sign * num
        return result
