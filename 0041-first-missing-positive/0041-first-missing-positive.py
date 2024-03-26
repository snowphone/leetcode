class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        poss = [i for i in nums if i > 0]
        if not poss:
            return 1
        m = min(poss)
        M = max(poss)
        if m > 1:
            return 1
        posset = set(poss)
        for i in range(m, M+2):
            if i in posset:
                continue
            return i
