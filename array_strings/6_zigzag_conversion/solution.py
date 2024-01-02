class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = []
        n = len(s)
        if numRows == 1 or n <= numRows:
            return s

        result = [[] for _ in range(numRows)]
        i = 0
        step = 1
        for c in s:
            result[i].append(c)
            if i == 0:
                step = 1
            elif i == numRows - 1:
                step = -1
            i += step

        return "".join("".join(row) for row in result)
