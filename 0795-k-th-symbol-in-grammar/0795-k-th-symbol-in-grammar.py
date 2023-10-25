class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def func(length, k) -> bool:
            if length == 1:
                return False
            
            if k <= length / 2:
                return func(length // 2, k)
            else:
                return not func(length // 2, k - length // 2)
        
        return int(func(2 ** (n - 1), k))
        
