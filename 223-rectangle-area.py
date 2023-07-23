class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        delta_w = min(ax2, bx2) - max(ax1, bx1)
        delta_h = min(ay2, by2) - max(ay1, by1)
        if delta_w <= 0 or delta_h <= 0:
            delta = 0
        else:
            delta = delta_w * delta_h
        area = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        area -= delta
        return area
