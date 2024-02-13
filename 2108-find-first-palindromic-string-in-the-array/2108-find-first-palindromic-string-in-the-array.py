class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        return next(
            (it for it in words if it == it[::-1]), ''
        )