from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        """
          0
          1
         10 2
         11
        100 4
        101
        110
        111

        result[i] = 1 + result[i - <largest power of 2 smaller than i>]
        result[5] = 1 + result[5 - 4]
        """
        if n == 0:
            return [0]
        target = 2
        result = [0, 1]
        for i in range(2, n + 1):
            if (i & (i - 1)) == 0:
                target = i
            result.append(1 + result[i - target])
        return result
