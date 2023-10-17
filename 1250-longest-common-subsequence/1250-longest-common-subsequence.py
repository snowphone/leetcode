class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @cache
        def fn(i: int, j: int):
            if i < 0 or j < 0:
                return 0
            
            it = text1[i]
            jt = text2[j]
            if it == jt:
                return fn(i-1, j-1) + 1

            return max(
                fn(i-1, j),
                fn(i, j-1),
            )

            
        return fn(len(text1) - 1, len(text2) - 1)