from functools import cmp_to_key

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        @cache
        def to_min(s: str):
            h = int(s[:2])
            m = int(s[3:])
            return h * 60 + m
        
        def diff(lhs: int, rhs: int):
            m = min(lhs, rhs)
            M = max(lhs, rhs)
            return min(
                M - m,
                24 * 60 + m - M,
            )

        timestamps = sorted(
            map(
                to_min,
                timePoints,
            )
        )

        answer = 24 * 60
        n = len(timestamps)
        for i in range(n):
            answer = min(
                answer,
                diff(timestamps[i], timestamps[(i+1)%n])
            )
        return answer