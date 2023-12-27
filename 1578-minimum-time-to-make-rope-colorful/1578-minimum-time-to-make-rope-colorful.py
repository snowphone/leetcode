class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        answer = 0
        i = 0
        while i < n:
            j = next(
                (k for k in range(i, n) if colors[k] != colors[i]), n
            )
            answer += sum(neededTime[i:j]) - max(neededTime[i:j])
            i = j
        return answer