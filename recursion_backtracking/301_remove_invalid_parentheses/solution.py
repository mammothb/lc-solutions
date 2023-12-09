import collections
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s):
            count = 0
            for c in s:
                if c == "(":
                    count += 1
                elif c == ")":
                    if count == 0:
                        return False
                    count -= 1
            return count == 0

        result = []
        found = False
        seen = set()
        valid_chars = {"(", ")"}
        queue = collections.deque([s])

        while queue:
            s = queue.popleft()
            if is_valid(s):
                result.append(s)
                found = True
            if not found:
                for i in range(len(s)):
                    if s[i] not in valid_chars:
                        continue
                    sub_str = s[:i] + s[i + 1 :]
                    if sub_str not in seen:
                        seen.add(sub_str)
                        queue.append(sub_str)
        if not result:
            return [""]
        return result

    def removeInvalidParentheses_dfs(self, s: str) -> List[str]:
        def is_valid(s):
            count = 0
            for c in s:
                if c == "(":
                    count += 1
                elif c == ")":
                    if count == 0:
                        return False
                    count -= 1
            return count == 0

        def dfs(s, start, l_count, r_count, result):
            if l_count == r_count and is_valid(s):
                result.append(s)
                return
            for i in range(start, len(s)):
                # Avoid processing the same removed string
                if i > start and s[i] == s[i - 1]:
                    continue
                if l_count > 0 and s[i] == "(":
                    dfs(s[:i] + s[i + 1 :], i, l_count - 1, r_count, result)
                elif r_count > 0 and s[i] == ")":
                    dfs(s[:i] + s[i + 1 :], i, l_count, r_count - 1, result)

        l_count = 0
        r_count = 0
        for c in s:
            if c == "(":
                l_count += 1
            if c == ")":
                if l_count > 0:
                    l_count -= 1
                else:
                    r_count += 1

        result = []
        dfs(s, 0, l_count, r_count, result)
        if not result:
            return [""]
        return result
