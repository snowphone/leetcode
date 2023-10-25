class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def func(n, k) -> bool:
            if n == 1:
                return False
            
            length = 2 ** (n - 1)
            
            if k <= length / 2:
                return self.kthGrammar(n-1, k)
            else:
                return not self.kthGrammar(n-1, k - length // 2)
        
        return int(func(n, k))
        
