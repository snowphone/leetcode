class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low_i = 0
        answer = 0
        for i, p in enumerate(prices):
            low_p = prices[low_i]
            if p < low_p:
                low_i = i
            answer = max(answer, p - low_p)
        return answer