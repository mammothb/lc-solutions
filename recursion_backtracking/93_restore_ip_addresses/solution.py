from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        self.solve(s, 0, len(s), [[]], result)
        return result

    def solve(self, s, start, stop, curr, result):
        if start == stop:
            if len(curr) != 4:
                return
            for elem in curr:
                if len(elem) > 3:
                    return
                if len(elem) > 1 and elem[0] == "0":
                    return
                if len(elem) > 2 and int("".join(elem)) > 255:
                    return
            result.append(".".join(["".join(elem) for elem in curr]))
            return

        # Add to current number if possible
        if len(curr[-1]) < 3:
            curr[-1].append(s[start])
            self.solve(s, start + 1, stop, curr.copy(), result)
            curr[-1].pop()
        # Start a new element if possible
        if len(curr) < 4 and curr[0]:
            curr.append([s[start]])
            self.solve(s, start + 1, stop, curr.copy(), result)
            curr.pop()
