class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        answer = 0
        banned = set(banned)

        for i in range(1, n+1):
            if i in banned:
                continue
            if i > maxSum:
                break
            maxSum -= i
            answer += 1

        return answer
            