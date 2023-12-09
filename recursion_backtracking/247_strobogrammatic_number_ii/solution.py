from typing import List


class Solution:
    """
    @param n: the length of strobogrammatic number
    @return: All strobogrammatic numbers
             we will sort your return value in output
    """

    map = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

    def find_strobogrammatic(self, n: int) -> List[str]:
        # write your code here
        def solve(k, is_even, curr, result):
            if k == 0:
                if curr[0] != "0":
                    result.append(curr)
                return
            for num in self.map:
                if k - 1 == 0 and num in {"6", "9"}:
                    continue
                solve(k - 1, is_even, curr + num, result)

        result = []
        solve((n + 1) // 2, n % 2 == 0, "", result)
        for i, prefix in enumerate(result):
            for j in range(n // 2 - 1, -1, -1):
                prefix += self.map[prefix[j]]
            result[i] = prefix
        if n == 1:
            result.append("0")
        return result

    def find_strobogrammatic_2(self, n: int) -> List[str]:
        def solve(k, n):
            if k == 0:
                return [""]
            if k == 1:
                return ["0", "1", "8"]

            centers = solve(k - 2, n)
            result = []
            for center in centers:
                if k != n:
                    result.append(f"0{center}0")
                result.append(f"1{center}1")
                result.append(f"6{center}9")
                result.append(f"8{center}8")
                result.append(f"9{center}6")
            return result

        return solve(n, n)
