class Solution:
    def minMovesToCaptureTheQueen(
        self, a: int, b: int, c: int, d: int, e: int, f: int
    ) -> int:
        # Diagonal check
        rook = (a, b)
        bishop = (c, d)
        queen = (e, f)

        if rook[0] == queen[0]:
            if rook[0] == bishop[0] and (
                rook[1] < bishop[1] < queen[1] or rook[1] > bishop[1] > queen[1]
            ):
                return 2
            return 1

        if rook[1] == queen[1]:
            if rook[1] == bishop[1] and (
                rook[0] < bishop[0] < queen[0] or rook[0] > bishop[0] > queen[0]
            ):
                return 2
            return 1

        # TRBL
        if bishop[0] + bishop[1] == queen[0] + queen[1]:
            if bishop[0] + bishop[1] == rook[0] + rook[1] and (
                bishop[0] < rook[0] < queen[0] or bishop[0] > rook[0] > queen[0]
            ):
                return 2
            return 1

        # TLBR
        if bishop[0] - bishop[1] == queen[0] - queen[1]:
            if bishop[0] - bishop[1] == rook[0] - rook[1] and (
                bishop[0] < rook[0] < queen[0] or bishop[0] > rook[0] > queen[0]
            ):
                return 2
            return 1

        return 2


# print(Solution().minMovesToCaptureTheQueen(1, 6, 3, 3, 5, 6))
# print(Solution().minMovesToCaptureTheQueen(1, 6, 8, 8, 3, 3))
print(Solution().minMovesToCaptureTheQueen(4, 4, 8, 8, 3, 3))
# print(Solution().minMovesToCaptureTheQueen(1, 6, 1, 5, 3, 3))
