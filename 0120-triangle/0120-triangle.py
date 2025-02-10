class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        depth = len(triangle)

        @cache
        def acc(level, idx):
            if level + 1 == depth:
                return triangle[level][idx]

            return triangle[level][idx] + min(
                acc(level + 1, idx),
                acc(level + 1, idx + 1),
            )

        return acc(0, 0)
