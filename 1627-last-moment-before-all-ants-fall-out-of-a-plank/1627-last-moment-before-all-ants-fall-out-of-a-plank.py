class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        cnt = len(left) + len(right)
        t = 0

        if left and right:
            return max( max(left), n - min(right) )
        elif left:
            return max(left)
        return n - min(right)