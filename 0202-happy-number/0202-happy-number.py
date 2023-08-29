class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set()
        def fn(n):
            if n == 1:
                return True
            if n in cache:
                return False

            cache.add(n)
            acc = 0
            while n:
                acc += (n % 10) ** 2
                n //= 10
            return fn(acc)

        return fn(n)
            
