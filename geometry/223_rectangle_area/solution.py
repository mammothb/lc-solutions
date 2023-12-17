class Solution:
    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        total_area = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        cx1 = max(ax1, bx1)
        cy1 = max(ay1, by1)
        cx2 = min(ax2, bx2)
        cy2 = min(ay2, by2)
        w = cx2 - cx1
        h = cy2 - cy1
        intersect_area = 0
        if w > 0 and h > 0:
            intersect_area = h * w
        return total_area - intersect_area
