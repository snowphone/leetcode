class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def fn(amount):
            if amount == 0:
                return 0
            if min(coins) > amount:
                return -1
            
            cands = []
            for coin in coins:
                tmp = fn(amount - coin)
                if tmp == -1:
                    continue
                cands.append(tmp + 1)
            return min(cands) if cands else -1
    
        return fn(amount)