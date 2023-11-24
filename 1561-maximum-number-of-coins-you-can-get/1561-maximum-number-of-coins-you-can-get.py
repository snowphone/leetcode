class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles) // 3
        piles.sort()
        
        acc = 0
        idx = -2
        for _ in range(n):
            acc += piles[idx]
            idx -= 2
        return acc