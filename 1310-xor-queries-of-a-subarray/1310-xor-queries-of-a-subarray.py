class Solution:

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        self.prefix_sum = []
        self._warm_up(arr)

        return [ self._xor(l, r) for l, r in queries ]

    def _warm_up(self, arr: List[int]): 
        self.prefix_sum = arr[:1]
        
        for it in arr[1:]:
            self.prefix_sum.append( it ^ self.prefix_sum[-1] )
        return

    def _xor(self, l: int, r: int):
        if l == 0:
            return self.prefix_sum[r]
        return self.prefix_sum[r] ^ self.prefix_sum[l-1]
        