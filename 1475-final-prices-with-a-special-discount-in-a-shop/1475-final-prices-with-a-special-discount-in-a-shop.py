class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = []
        n = len(prices)
        for i, it in enumerate(prices):
            jt = next(
                ( prices[k] for k in range(i+1, n) if prices[k] <= it ), 0
            )
            answer.append(it - jt)
        return answer