from typing import List


class Solution:
    opset = {"+", "-", "*", "/"}

    def evalRPN(self, tokens: List[str]) -> int:
        ops = []
        nums = []
        counts = [0]  # store an extra count for the answer
        while tokens:
            char = tokens.pop()
            if char in self.opset:
                ops.append(char)
                counts.append(0)
            else:
                nums.append(int(char))
                counts[-1] += 1
            # Start computing when we reach the 2 inputs requirement
            while counts[-1] == 2:
                left = nums.pop()
                right = nums.pop()
                op = ops.pop()
                if op == "+":
                    nums.append(left + right)
                elif op == "-":
                    nums.append(left - right)
                elif op == "*":
                    nums.append(left * right)
                else:
                    nums.append(int(left / right))
                counts.pop()
                counts[-1] += 1
        return nums[0]

    def evalRPN_left_to_right(self, tokens: List[str]) -> int:
        nums = []
        for c in tokens:
            if not c in self.opset:
                nums.append(int(c))
            else:
                right = nums.pop()
                left = nums.pop()
                if c == "+":
                    nums.append(left + right)
                elif c == "-":
                    nums.append(left - right)
                elif c == "*":
                    nums.append(left * right)
                else:
                    nums.append(int(left / right))
        return nums[-1]
