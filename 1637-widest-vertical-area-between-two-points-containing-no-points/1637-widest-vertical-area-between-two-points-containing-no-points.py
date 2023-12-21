class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        widths = [x for x, y in points]
        widths.sort()

        answer = 0
        for i, j in zip(widths, widths[1:]):
            answer = max(answer, j - i)
        return answer