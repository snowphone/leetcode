class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        area = lambda: (j-i) * min(height[i], height[j])
        answer = area()

        while i < j:
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
            answer = max(answer, area())
        return answer