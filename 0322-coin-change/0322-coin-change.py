from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        coins.sort(reverse=True)

        @cache
        def fn(idx: int, target: int):
            if target == 0:
                return 0
            if target < 0 or idx == n:
                return -1
            
            tmp1 = fn(idx, target - coins[idx])
            if tmp1 != -1:
                tmp1 += 1
            tmp2 = fn(idx + 1, target)

            if tmp1 >= 0 and tmp2 >= 0:
                return min(tmp1, tmp2)
            elif tmp1 >= 0:
                return tmp1
            elif tmp2 >= 0:
                return tmp2
            return -1

        return fn(0, amount)
        