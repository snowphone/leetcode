class Solution:
    def largestRectangleArea(self, heights):
        stk = []  # Invariant: q[i] < q[i+1]

        def invariant(height: int):
            top_idx = stk[-1]
            return heights[top_idx] < h

        answer = 0
        for r, h in enumerate(heights + [0]):
            while stk and not invariant(h):
                height = heights[stk.pop()]
                width = r - (stk[-1] + 1) if stk else r
                answer = max(answer, height * width)
            stk.append(r)
        return answer
