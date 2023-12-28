class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        part = ""
        for c in f"{path}/":
            if c == "/":
                if stack and part == "..":
                    stack.pop()
                elif part not in ("", ".", ".."):
                    stack.append(part)
                part = ""
            else:
                part += c
        return f"/{'/'.join(stack)}"
