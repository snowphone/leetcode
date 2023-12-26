class Solution:
    @cache
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n == 1:
            return 1 if 1 <= target <= k else 0

        if target <= 0:
            return 0
        
        MOD = 10 ** 9 + 7
        
        return sum(
            self.numRollsToTarget(n-1, k, target - i)
            for i in range(1, k+1)
        ) % MOD