class Solution:
    def calculate(self, s: str) -> int:
        def solve(s, idx, n):
            def update_stack(stack, sign, num):
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))

            stack = []
            num = 0
            sign = "+"

            while idx < n:
                if s[idx].isdigit():
                    num = 10 * num + int(s[idx])
                elif s[idx] in "+-*/":
                    update_stack(stack, sign, num)
                    sign = s[idx]
                    num = 0
                idx += 1
            update_stack(stack, sign, num)
            return sum(stack)

        return solve(s, 0, len(s))
