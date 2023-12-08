class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def dist(a, b):
            return max(
                abs(a[0] - b[0]),
                abs(a[1] - b[1]),
            )
        
        acc = 0
        for a, b in zip(points, points[1:]):
            acc += dist(a, b)
        return acc