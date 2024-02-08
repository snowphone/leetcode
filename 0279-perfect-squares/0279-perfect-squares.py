class Solution:
    def numSquares(self, n: int) -> int:
        perfs = [i**2 for i in range(1, 10 ** 2 + 1)]

        @cache
        def fn(n: int):
            if n in perfs:
                return 1
            
            answer = 987654321
            for i in perfs:
                if i >= n:
                    break
                answer = min(
                    answer,
                    1 + fn(n-i)
                )
            return answer
        return fn(n)