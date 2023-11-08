class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        min_dist = max(abs(sx-fx), abs(sy - fy))

        if sx == fx and sy == fy:
            return t != 1
        return  min_dist <= t