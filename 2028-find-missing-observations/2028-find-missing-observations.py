class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total_sum = mean * (n + m)
        total_sum -= sum(rolls)

        if not (1 * n <= total_sum <= 6 * n):
            return []

        answer = [(total_sum // n) for _ in range(n)]
        total_sum -= (total_sum // n) * n

        for i in range(n):
            if not total_sum:
                break
            gap = 6 - answer[i]
            if gap <= total_sum:
                answer[i] += gap
                total_sum -= gap
            else:
                answer[i] += total_sum
                total_sum = 0
        return answer 
            
        