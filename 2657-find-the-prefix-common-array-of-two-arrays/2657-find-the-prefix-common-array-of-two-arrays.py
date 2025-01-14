class Solution:
    def findThePrefixCommonArray(self, a: List[int], b: List[int]) -> List[int]:
        n = len(a)
        return [
            len(set(a[:i]) & set(b[:i])) for i in range(1, n+1)
        ]