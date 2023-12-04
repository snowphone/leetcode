class Solution:
    def largestGoodInteger(self, num: str) -> str:
        numstr = str(num)
        return next(
            (it for i in range(9, -1, -1) if (it := str(i) * 3) in numstr), ''
        )
        