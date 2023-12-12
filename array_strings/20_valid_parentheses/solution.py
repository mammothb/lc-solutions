class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # contains opening brackets
        bracket = {"(": ")", "[": "]", "{": "}"}
        for c in s:
            if c in bracket:
                stack.append(c)
            else:
                if stack:
                    close = bracket[stack.pop()]
                    if close != c:
                        return False
                else:  # At a closing bracket but no opening to match
                    return False

        return not stack
