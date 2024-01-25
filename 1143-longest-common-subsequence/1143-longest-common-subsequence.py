class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @cache
        def common(i: int, j: int):
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                return 1 + common(i-1, j-1)
            return max(
                common(i-1, j),
                common(i, j-1),
            )
        return common(
            len(text1) - 1, len(text2) - 1
        )