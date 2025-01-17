from functools import reduce
import operator

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        """
        d[i] = x[i] ^ x[i+1]
        x[i+1] = d[i] ^ x[i]
        x[i+1] = d[i] ^ (d[i-1] ^ x[i-1])
        ...
        x[i+1] = d[i] ^ (d[i-1] ^ x[i-1]) ^ ...^ d[0] ^ x[0]

        Therefore, the `x` must satisfy x[n] = reduce(xor, d[0..n-1]) ^ x[0]
        """
        xor = lambda iter: reduce(operator.xor, iter)
        n = len(derived)

        acc = xor(derived)

        def try_with(start_value: int):
            return start_value == (acc ^ start_value)
        
        return try_with(0) or try_with(1)
        