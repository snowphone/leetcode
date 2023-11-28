class Solution:
    def knightDialer(self, n: int) -> int:
        mapping = [
            [4,6],
            [6,8],
            [7,9],
            [4,8],
            [0,3,9],
            [],
            [0,1,7],
            [2,6],
            [1,3],
            [2,4],
        ]
        
        MOD = 10 ** 9 + 7
        
        @cache
        def fn(sz, pos):
            if sz == 1:
                return 1
            
            return sum(
                fn(sz-1, it) for it in mapping[pos]
            ) % MOD
        
        return sum(
            fn(n, it) for it in range(10)
        ) % MOD
            

            